### minikube start 

```
W0514 02:06:29.789088   30204 main.go:291] Unable to resolve the current Docker CLI context "default": context "default": context not found: open C:\Users\samkh\.docker\contexts\meta\37a8eec1ce19687d132fe29051dca629d164e2c4958ba141d5f4133a33f0688f\meta.json: The system cannot find the path specified.
😄  minikube v1.33.0 on Microsoft Windows 10 Pro 10.0.19045.4291 Build 19045.4291
✨  Automatically selected the docker driver. Other choices: hyperv, ssh
📌  Using Docker Desktop driver with root privileges
👍  Starting "minikube" primary control-plane node in "minikube" cluster
🚜  Pulling base image v0.0.43 ...
💾  Downloading Kubernetes v1.30.0 preload ...
    > preloaded-images-k8s-v18-v1...:  342.90 MiB / 342.90 MiB  100.00% 3.87 Mi
    > gcr.io/k8s-minikube/kicbase...:  480.29 MiB / 480.29 MiB  100.00% 3.91 Mi
🔥  Creating docker container (CPUs=2, Memory=1964MB) ...
🐳  Preparing Kubernetes v1.30.0 on Docker 26.0.1 ...
    ▪ Generating certificates and keys ...
    ▪ Booting up control plane ...
    ▪ Configuring RBAC rules ...
🔗  Configuring bridge CNI (Container Networking Interface) ...
🔎  Verifying Kubernetes components...
    ▪ Using image gcr.io/k8s-minikube/storage-provisioner:v5
🌟  Enabled addons: storage-provisioner, default-storageclass
🏄  Done! kubectl is now configured to use "minikube" cluster and "default" namespace by default
```


### Inside WSL ==> [E:\python-microservices\system-design\python\src\auth] ==> Run

```
> cd /mnt/folder

> python -m venv venv

> source ./venv/Scripts/Activate

or

> source ./venv/bin/Activate

### Check the virtual environment
> env | grep VIRTUAL
```

### IN POWER SHELL ==> run

https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_scripts?view=powershell-7.4&viewFallbackFrom=powershell-6#script-scope-and-dot-sourcing

https://medium.com/artificialis/virtualenv-and-local-environment-in-python-and-pip-424c68d8bc2d

> . venv\scripts\Activate.ps1

or 

```
> pip install virtualenv
> virtualenv .venv
```

or

> pipenv shell

#### DEACTIVATE virtual environment

> deactivate

### Check VIRTUAL env by Checkout PIP List ==> Run it before and after enabling the virtual env

>  pip list


### Sharing virtual environment

> pip freeze > requirements.txt

### Installing packages from others

> pip install -r requirements.txt


### install utility packages using pip

```
> pip install pylint

> pip install jedi

> pip install pyjwt

> pip install flask

> pip install flask_mysqldb

```

### setup env in shell

> export MYSQL_HOST=localhost

### get env that is set using shell

> os.environ.get("MYSQL_HOST")

