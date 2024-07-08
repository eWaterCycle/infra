"""Convert raw ERA5 data to esmvaltool compatible format.

Usage:

    python roles/prep_shared_data/files/era5process.py 1990 total_precipitation pr obs6/Tier3/ERA5/OBS6_ERA5_reanaly_1_day_pr_1990-1990.nc
"""

import argparse
from pathlib import Path
from esmvalcore.dataset import Dataset
from esmvalcore.preprocessor import extract_time, daily_statistics
import xarray as xr
import numpy as np

parser = argparse.ArgumentParser(description='Process ERA5 data')
parser.add_argument('year', type=int, help='Current year')
parser.add_argument('era5_name', type=str, help='ERA5 name of the variable')
parser.add_argument('short_name', type=str, help='Short name of the variable')
parser.add_argument('output', type=str, help='Output file')

args = parser.parse_args()

print(f'Processing ERA5 {args.era5_name} data from year {args.year} to {args.short_name} and saving to {args.output}')

# When raw files are in . then uncomment below
# CFG['rootpath'] = {
#     'default': '.',
# }

current_year = args.year
var = args.short_name

eds = Dataset(
    project='native6',
    dataset='ERA5',
    type='reanaly',
    version='v1',
    tier=3,
    timerange=f'{current_year}/{current_year + 1}',
    short_name=var,
    mip='E1hr',
    era5_name=args.era5_name,
    era5_freq='hourly',
)
eds.find_files()
orig_file = eds.files[0]

def unit_and_encoding(fn: str) -> tuple[str, dict]:
    with xr.open_dataarray(fn) as da:
        return da.attrs['units'], da.encoding


orig_unit, orig_encoding = unit_and_encoding(orig_file)

cube = eds.load()

print(f'Loaded data from {eds.files}')

# Do + first day of next year
cube = extract_time(cube, start_year=current_year, start_month=1, start_day=1, end_year=current_year + 1, end_month=1, end_day=1)
print('Extracted time')
# Do mean or max or min
operator = 'mean'
if var.endswith('max'):
    operator = 'max'
if var.endswith('min'):
    operator = 'min'
cube = daily_statistics(cube, operator='mean')

print(f'Computed daily {operator} statistics')

da = xr.DataArray.from_iris(cube)

print('Converted to xarray')

new_unit = da.attrs['units']

def compute_encoding(da: xr.DataArray) -> dict:
    vmin = da.min().values.tolist()
    vmax = da.max().values.tolist()
    offset = (vmax - vmin)/2 + vmin
    scale_factor = np.max([vmin - offset, offset - vmin])/2**15 * 1.01 # room for nans
    return {
        'dtype': 'int16',
        '_FillValue': np.iinfo(np.int16).min,
        "missing_value": np.iinfo(np.int16).min,
        'scale_factor': scale_factor,
        'add_offset': offset,
    }

if new_unit == orig_unit:
    da.encoding = orig_encoding
else:
    da.encoding = compute_encoding(da)

# what: Compression vs no compression zlib l4
# write: 14 minutes vs 1 minute
# size: 350Mb vs 760Mb
# See https://docs.xarray.dev/en/stable/user-guide/io.html#chunk-based-compression
da.encoding['zlib'] = True
da.encoding['complevel'] = 4 # 4 is the default in netcdf4 library
da.encoding['shuffle'] = True
# Chunk with whole year of a spatial areas as we are going to generate forcing for a certain area and whole year
# da.encoding['chunksizes'] = (365, 80, 160) # chunk size ~18Mb, nr 90

# TODO try blosc_lz4 and sz3 from h5plugin, but should be esmvaltool compatible
# da.encoding['zlib'] = False
# da.encoding['blosc_lz4'] = True
# da.encoding['complevel'] = 5
# da.encoding['shuffle'] = True
# Same size time as uncompressed

# da.encoding['zlib'] = False
# da.encoding['blosc_lz4'] =  False
# da.encoding['sz3'] = True
# da.encoding['complevel'] = 5
# da.encoding['shuffle'] = True
# Gives TypeError: Compression method must be specified

print(f'Saving file to {args.output}')
# Save file
Path(args.output).parent.mkdir(parents=True, exist_ok=True)
da.to_netcdf(args.output, format='NETCDF4', engine='netcdf4')
# For fancy compression use h5 engine
# da.to_netcdf(args.output, format='NETCDF4', engine='h5netcdf')

# TODO check output can be read by esmvaltool
