Docs: https://www.unidata.ucar.edu/software/thredds/current/tds/TDS.html

Docker: https://github.com/Unidata/thredds-docker

# RUN

Populate `data/` dir with eWatercycle1 output dataset.

```bash
docker run -ti -v $PWD/data:/data \
 -v $PWD/config/catalog.xml:/usr/local/tomcat/content/thredds/catalog.xml \
 -v $PWD/config/threddsConfig.xml:/usr/local/tomcat/content/thredds/threddsConfig.xml \
 -v $PWD/config/wmsConfig.xml:/usr/local/tomcat/content/thredds/wmsConfig.xml \
 -p 8080:8080 unidata/thredds-docker
```

Goto http://localhost:8080/thredds/catalog.html

# Crawl

```bash
pip install thredds_crawler
```

Modify `site-packages/thredds_crawler/crawl.py` to work sequentially:
```diff
119,120c119,120
<         jobs = [self.pool.apply_async(make_leaf, args=(url, auth)) for url in urls]
<         datasets = [j.get() for j in jobs]
---
>         jobs = [make_leaf(url, auth) for url in urls]
>         datasets = [j for j in jobs]

```

```python
from thredds_crawler.crawl import Crawl
c = Crawl('http://localhost:8080/thredds/catalog.xml')
print c.datasets
[<LeafDataset id: ewc/2017-11-21/work01/output/netcdf/totalEvaporation_dailyTot_output.nc, name: totalEvaporation_dailyTot_output.nc, services: ['OPENDAP', 'DAP4', 'HTTPServer', 'WCS', 'WMS', 'NetcdfSubset']>,
 <LeafDataset id: ewc/2017-11-21/work01/output/netcdf/satDegUppSurface_dailyTot_output.nc, name: satDegUppSurface_dailyTot_output.nc, services: ['OPENDAP', 'DAP4', 'HTTPServer', 'WCS', 'WMS', 'NetcdfSubset']>,
 <LeafDataset id: ewc/2017-11-21/work01/output/netcdf/discharge_dailyTot_output.nc, name: discharge_dailyTot_output.nc, services: ['OPENDAP', 'DAP4', 'HTTPServer', 'WCS', 'WMS', 'NetcdfSubset']>]
```