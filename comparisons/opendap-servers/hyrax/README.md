Reference OpenDAP

https://www.opendap.org/software/hyrax-data-server

https://github.com/OPENDAP/hyrax-docker

# Run

Populate `data/` dir with eWatercycle1 output dataset.

```
docker run -ti -e NCWMS_BASE=http://localhost:8080 -p 8080:8080 -v $PWD/data:/usr/share/hyrax opendap/hyrax_ncwms
```

Goto http://localhost:8080/opendap/

