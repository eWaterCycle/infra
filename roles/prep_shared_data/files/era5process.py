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
cube = ds.load()

# Do + first day of next year
cube = extract_time(cube, start=f'{current_year}-01-01', end=f'{current_year + 1}-01-01')
# Do mean or max or min
cube = daily_statistics(cube, operator='mean')
# TODO for taxmin and taxmax, we need to do the daily max and min

# Save file
save(cube, args.output, zlib=True)
