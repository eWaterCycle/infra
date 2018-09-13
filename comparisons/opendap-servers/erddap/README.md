https://coastwatch.pfeg.noaa.gov/erddap/index.html

# Run

```
docker run -ti -v $PWD/data:/data \
 -v $PWD/config/setup.xml:/usr/local/tomcat/content/erddap/setup.xml \
 -v $PWD/config/datasets.xml:/usr/local/tomcat/content/erddap/datasets.xml \
 -p 8080:8080 \
 axiom/docker-erddap
```

Goto http://localhost:8080/erddap/

On first page load the indexing of datasets is triggered which means initially there are zero datasets, reload page to see datasets.

# Config

Generate xml blurp from *.nc files with 
```
cd webapps/erddap/WEB-INF
bash GenerateDatasetsXml.sh
Which EDDType (default="EDDGridFromNcFiles")
? 
Parent directory (default="/data")
? 
File name regex (e.g., ".*\.nc") (default="satDegUppSurface_dailyTot_output.nc")
? discharge_dailyTot_output.nc
Full file name of one file (or leave empty to use first matching fileName) (default="")
? 
ReloadEveryNMinutes (e.g., 10080) (default="")
? 

Repeat for each type of variable.
Copy xml output into `config/datasets.xml`.
