import argparse
from esmvalcore.dataset import Dataset
from esmvalcore.config import CFG
from esmvalcore.preprocessor import extract_time, daily_statistics
from iris import save

parser = argparse.ArgumentParser(description='Process ERA5 data')
parser.add_argument('year', type=int, help='Current year')
parser.add_argument('short_name', type=str, help='Short name of the variable')
parser.add_argument('era5_name', type=str, help='ERA5 name of the variable')
parser.add_argument('output', type=str, help='Output file')

args = parser.parse_args()

print(f'Processing ERA5 data from {args.currentyear} with first day of {args.nextyear} to {args.output}')

CFG['rootpath'] = {
    'default': '.'
}

current_year = args.year

ds = Dataset(
    project='native6',
    dataset='ERA5',
    type='reanaly',
    version='v1',
    tier=3,
    timerange=f'{current_year}/{current_year + 1}',
    short_name=args.short_name,
    mip='E1hr',
    era5_name=args.era5_name,
    era5_freq='hourly',
)
ds.find_files()
xds = xarray.open_dataset(ds.first_file, chunks=auto)
encoding = xsd[args.era5_name].encoding
rawunit = xsd[args.era5_name].attrs.unit
xds.close()
cube = ds.load()

# Do + first day of next year
cube = extract_time(cube, start=f'{current_year}-01-01', end=f'{current_year + 1}-01-01')
# Do mean or max or min
cube = daily_statistics(cube, operator='mean')
# TODO for taxmin and taxmax, we need to do the daily max and min

def get_encoding(data: xr.DataArray) -> dict[str, str]:
    vmin = data.min()
    vmax = data.max()
    offset = (vmax - vmin)/2 + vmin
    scale_factor = np.max([vmin - offset, offset - vmin])/2**15 * 1.01 # room for nans
 
    return {
        "dtype": np.dtype("int16"),
        "missing_value": -32767,
        "_FillValue": -32767,
        "scale_factor": float(scale_factor),
        "add_offset": float(offset),
        "zlib": True,
        "complevel": 7,
        "shuffle": True,
        # Chunksize time in single chunk or -1, chunks around 10Mb
        "chunksizes": (24, 40, 70),
    }
 
encoding = {}
for var in ds.data_vars:
    encoding[var] = get_encoding(ds[var])

# Save file
xds2 = xarray.from_iris(cube)
encoding[zlib] = true
enconding[complevel] = 5 
newunit = xsd2[args.short_name].attrs.unit
if newunit != oldunit:
    xsd2[args.short_name].encoding = encoding
else:
    xsd2[args.short_name].encoding = get_encoding( xsd2[args.era5_name])
    # derive center / offset 
xds2.to_netcdf(args.output)
# save(cube, args.output, zlib=True)
