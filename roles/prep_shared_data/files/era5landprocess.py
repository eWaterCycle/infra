import argparse
from esmvalcore.dataset import Dataset
from esmvalcore.config import CFG

from iris import save

parser = argparse.ArgumentParser(description='Process ERA5 data')
parser.add_argument('output', type=str, help='Output file')

args = parser.parse_args()

print(f'Processing ERA5 land data to {args.output}')

CFG['rootpath'] = {
    'default': '.'
}

ds = Dataset(
    project='native6',
    dataset='ERA5',
    type='reanaly',
    version='v1',
    tier=3,
    short_name='orog',
    mip='fx',
    era5_name='z',
)
ds.find_files()
cube = ds.load()

# Save file
save(cube, args.output, zlib=True)
