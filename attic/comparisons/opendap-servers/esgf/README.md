Setup esgf for eWaterCycle forecast

# Start stack

Follow https://cedadev.github.io/esgf-docker/usage/quick-start/

```bash
git clone https://github.com/cedadev/esgf-docker.git
cd esgf-docker
mkdir data config
export ESGF_HOSTNAME=192.168.81.3.xip.io
export ESGF_CONFIG=$PWD/config
export ESGF_DATA=$PWD/data
docker-compose pull

docker-compose run esgf-setup generate-secrets
docker-compose run esgf-setup generate-test-certificates
docker-compose run esgf-setup create-trust-bundle
sudo chmod +rx config/certificates/*/*.key

docker-compose up -d
```

Esgf node running at https://192.168.81.3.xip.io

# Publish test dataset

Follow https://cedadev.github.io/esgf-docker/usage/publishing/

Datafile at https://192.168.81.3.xip.io/search/testproject/

# Publish eWaterCycle

mkdir -p data/ewatercycle
cp -r /media/sf_data/eWaterCycle2/2017-11-21 data/ewatercycle/
chmod R +rx data
