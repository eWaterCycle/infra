Setup JupyterHub using https://zero-to-jupyterhub.readthedocs.io (kubernetes) with [minikube](https://kubernetes.io/docs/getting-started-guides/minikube/)

# Minikube

See https://kubernetes.io/docs/getting-started-guides/minikube/

```bash
curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl
chmod +x kubectl 
curl -Lo minikube https://storage.googleapis.com/minikube/releases/v0.25.2/minikube-linux-amd64 && chmod +x minikube
sudo cp minikube kubectl /usr/local//bin/
# increase mem as default=2048 resulted in out of memory when trying to start a lab
minikube start --memory=8096 --cpus=4
# shadow local docker installation with minikube docker installation
eval $(minikube docker-env)
kubectl config use-context minikube
```

For Windows use [choco](https://chocolatey.org)
```powershell
choco install Minikube kubernetes-cli kubernetes-helm docker
```

# Helm

See https://zero-to-jupyterhub.readthedocs.io/en/latest/setup-helm.html#setup-helm

Install
```bash
curl https://raw.githubusercontent.com/kubernetes/helm/master/scripts/get | bash
```

Init
```bash
kubectl --namespace kube-system create serviceaccount tiller
# dont do below as minikube does not use rbac
# kubectl create clusterrolebinding tiller --clusterrole cluster-admin --serviceaccount=kube-system:tiller
helm init --service-account tiller
helm version
```

# JupyterHub

```
helm repo add jupyterhub https://jupyterhub.github.io/helm-chart/
helm repo update
helm install jupyterhub/jupyterhub \
    --version=v0.6 \
    --name=ewc-hub \
    --namespace=ewc \
    -f config.yaml
kubectl --namespace=ewc get pod
kubectl --namespace=ewc get svc
minikube dashboard
minikube service -n ewc proxy-public
```

Login as someone:someone and start server

# Customize

Create config file by copying `config2.yaml.template` to `config2.yaml` and following instructions inside.

Enable Github auth and lab
```
helm upgrade ewc-hub jupyterhub/jupyterhub --version=v0.6 -f config2.yaml
```

Now login with your GitHub account and server is running in lab mode.

Make sure the running hub and the callback url on https://github.com/settings/developers and are the same.

# Dask

## Helm

Run dask cluster next to existing pods, see https://dask.pydata.org/en/latest/setup/kubernetes-helm.html

```
cat dask.yaml 
jupyter:
  enabled: false

helm repo update
helm install stable/dask --namespace=ewc --name=dask -f dask.yaml
# Dask dashboard
minikube service -n ewc dask-scheduler
kubectl --namespace=ewc get svc dask-scheduler
```

In notebook
```python
from dask.distributed import Client
# adress = <CLUSTER-IP>:<FIRST PORT from PORTS column>
# eg 8786:32187/TCP,80:30272/TCP
adress = '10.104.29.96:8786'
client = Client(adress)
```

Check versions
```
client.get_versions(check=True)
```

Sync client version with rest in terminal with:
```
pip install blosc
pip install dask==0.17.1 distributed==1.21.1
pip install bokeh==0.12.14 cloudpickle==0.5.2 msgpack==0.5.5 numpy==1.14.1 pandas==0.22.0
conda install -y graphviz
pip install graphviz
```

Run example dask from https://github.com/dask/dask-docker/blob/master/notebook/examples/04-dask-array.ipynb
```python
from dask.distributed import progress
import dask.array as da
x = da.random.random(size=(10000, 10000), chunks=(1000, 1000))
x

x = x.persist()

x.sum().visualize()
x.sum().compute()

x[x < 0] = 0
x[x > x.mean(axis=0)] = 1
y = x + x.T
da.diag(y).visualize()

da.diag(y).compute()
```

```
helm delete dask --purge
```

## dask-kubernetes

https://dask-kubernetes.readthedocs.io/en/latest/

Not applicable, python code must run in env with kubernetes client config.

# Call API as service

Create config file by copying `config3.yaml.template` to `config3.yaml` and following instructions inside.

Add an external service with a known token

```
helm upgrade ewc-hub jupyterhub/jupyterhub --version=v0.6 -f config3.yaml
```

In Python shell outside kubernetes enviroment.
(replace ip-adress:port with current running hub)
```
import requests
# Token from config3.yaml
token = 'd823a82f5f6811032fbefba1b3c670de53066c9cc554a93014b3b9b68262fef8'
api_url = 'http://192.168.99.101:32632/hub/api'
s = requests.Session()
s.headers = {'Authorization': 'token %s' % token}

# List users
s.get(api_url + '/users').json()

# Start a server
r = s.post(api_url + '/users/sverhoeven/server')
r
<Response [201]>
```

Server was started successfully.

Create document in lab using token of service in someones server
```
lab_url = 'http://192.168.99.101:32632/user/sverhoeven/api'
s.get(lab_url + '/status').json()
r = s.put(lab_url + '/contents/mynewfile.txt', json={'type': 'file', 'format': 'text', 'content': 'some content'})

r = s.put(lab_url + '/contents/experiment1', json={'type': 'directory'})
r = s.put(lab_url + '/contents/experiment1/mynewfile.txt', json={'type': 'file', 'format': 'text', 'content': 'some content'})
```

# Clean up

```bash
minikube stop
```
