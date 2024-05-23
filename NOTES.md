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
> SET MYSQL_HOST=localhost

### get env that is set using shell

> os.environ.get("MYSQL_HOST")


### create new file in powershell | ni = New-item
> ni <file_name>

### Get into MySQL DB

> mysql -u<MySQL_USER> -p<MySQL_PASS>

### Run a SQL scripts from command line | bash-terminal

> mysql -u<MySQL_USER> -p<MySQL_PASS> < init.sql

### Drop a DATABASE using command line | bash-terminal

> mysql -u<MySQL_USER> -p<MySQL_PASS> -e "DROP DATABASE auth_py_micro"

### Drop a USER using command line | bash-terminal

> mysql -u<MySQL_USER> -p<MySQL_PASS> -e "DROP USER py_micro_user@localhost"

### Show table columns

> describe <table_name>;

### basic authentication consists of username and password and encoded with base64 into Authorization header

> Authorization: Basic base64(username:password)

### JSON Web Token

> Authorization: Bearer <Token> 

1.It has Two formatted JSON string with a signature

    1. Header: Algorithm and Token Type
    ```
        {
            "alg": "HS256",
            "typ": "JWT"
        }
    ```

        1. There can be two types of signing algorithm

            1. Asymmetric Algorithm, 
            which means there are two keys: one public key and one private key that must be kept secret. Auth0 has the private key used to generate the signature, and the consumer of the JWT retrieves a public key from the metadata endpoint provided by Auth0 and uses it to validate the JWT secret.

            2. (HS25 - HMAC with SHA-256) Symmetric Algorithm, 
            which means that there is only one private key that must be kept secret, and it is shared between the two parties


    2. Payload: Data. It contains CLAIMS for the users or the BEARER of the token. pieces of information about the user. 
        The most part token can be defined manually but some claims such as "issuer of the token" or "expiration of the token" can be predefined.
    ```
        {
            "sub": "12345",
            "name": "John Doe",
            "lat": "14.563214"
        }
    ```    

    3. Verify Signature: it comprises three part and each part is base64 encoded. All three parts are merged together and separated by a single dot (.) | Here signing algorithm is "HMACSHA256"
    ```
        HMACSHA256(
            base64UrlEncoded(header) + "." + base64UrlEncoded(payload) + "." + base64UrlEncoded(256-bit-secret)
        )
    ```

#### if we don't define host, it will be default to localhost which means the api wont be available outside
#### defining host to 0.0.0.0 will make the api available to all public IPs
#### When IP address assigned to a Docker container, it means it is assigned within a Docker Network that is where the host config in flask app under server run comes in where we set it to 0.0.0.0 to listen to all publics IPs which includes the Docker Container IP. Docker Container IPs address changes and it's not static so we need to define the server host as such kind of like wild card. If we do not define it then it will be default to loop back address, localhost, which can only be accessed from the host

# Dockerfile
### 1. Each instruction in a Dockerfile, resolves in a single new images layer being created.
### 2. So each layer creates on top of another images
### 3. If a layer is changed, then all the layers proceeding it will be rebuild

## Build a Docker Image
> docker build .

## Tag and push a docker image

> docker tag <local_image's_sha256> <registry_repo>:<tag_name>

>  docker push <registry_repo>:<tag_name>

## DIR <manifests> will hold all the kubernetes config | all files under it will be yaml

https://spacelift.io/blog/kubernetes-deployment-yaml

### start minikube
> minikube start
### star K9s
> k9s

# Docker system prune

> docker system prune

### it will remove
  - all stopped containers
  - all networks not used by at least one container
  - all dangling images
  - unused build cache

```
minikube delete

minikube start
```

# to run the infrastructure code from yaml | go to the folder that contains yamls

> kubectl apply -f ./

# to get the MYSQL variable in shell

> env | grep MYSQL

# WHAT is KUBERNETES
### It is a tool to automate the manual task for containerized apps.

https://kubernetes.io/docs/concepts/overview/working-with-objects/

## To scale the kubernetes pods
> kubectl scale deployment --replicas=6 service

## kubectl CLI interfacing with the Kubernetes API and do the CRUD operation to K8s Clusters' objects in the background for us