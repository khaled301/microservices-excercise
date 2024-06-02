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
        The most part token can  be defined manually but some claims such as "issuer of the token" or "expiration of the token" can be predefined.
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

# To shutdown replicas in the k9s
> kubectl scale deployment --replicas=0 gateway

# to get the MYSQL variable in shell

> env | grep MYSQL

# WHAT is KUBERNETES
### It is a tool to automate the manual task for containerized apps.

https://kubernetes.io/docs/concepts/overview/working-with-objects/

## To scale the kubernetes pods
> kubectl scale deployment --replicas=6 service

## kubectl CLI interfacing with the Kubernetes API and do the CRUD operation to K8s Clusters' objects in the background for us

#### flash pymongo
https://flask-pymongo.readthedocs.io/en/latest/


# Key terms

### Asynchronous and Synchronous
#### Interservice Communication

### strong and eventual
#### Consistency

# RabbitMQ
#### links
1. https://www.rabbitmq.com/tutorials/amqp-concepts
2. https://www.rabbitmq.com/docs/queues

### Simple RabbitMQ Queue architecture
1. Producer ==> exchange
2. Exchange ==> queues (routing key)
3. Queues ==> consumers (round robin)
4. Consumers

### To avoid bottle-necking of the consumer we can use competing consumers pattern

#### this pattern simply enables the multiple concurrent consumers to process messages received in the same messaging channel. It will increase throughput if the queues is full of message

#### by default the RabbitMQ will dispatch messages to the consuming services using the Round Robin algorithm


#### When we publish a message in the RabbitMQ queue using channel. We must make sure the the message itself is durable along with queue itself. Otherwise it will be lost if pod crashes or restarts

### Setting up the PERSISTENT_DELIVERY_MODE, under the properties, is important for durability of each message
```
    channel.basic_publish(
        exchange="",
        routing_key="video",
        body=json.dumps(message),
        properties=pika.BasicProperties(
            delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
        )
    )
```


##
1. build docker image
2. tag docker image
3. push to docker hub
4. create k8s manifests
5. add deployment config yaml 


### In K8 the service name resolve into that service's host ip address

> AUTH_SVC_ADDRESS: "auth:5000"

### in K8s contest the Service is just a group of pods. The service exists in a cluster inside a private network

### To allow request from outside to hit the services' endpoint. 
### To do this we can use [Ingress Controller] <ingress.yaml> which consists of load-balancer which essentially the entry point of the cluster and set of rules. The rules defines which request will go where. For instance, Ingress can direct to the internal service using cluster ip based on the request domain.
### we can use <nginx> to handle the load balancer portion of the Ingress

### for development, we need to map an custom address to our loopback address(127.0.0.1), the localhost ip, so that it can hit ingress load balancer endpoint
### To do that in WINDOWS
1. Navigate to C:\Windows\System32\drivers\etc.
    - in Powershell
    - - notepad C:\Windows\System32\drivers\etc\hosts
2. In the "Open" dialog, change the file type from "Text Documents (.txt)" to "All Files (.*)" so you can see the hosts file.
3. Select hosts and click Open.
4. Add a new line with the following format:
    > 127.0.0.1 yourdomain.com
5. save
6. Some browsers and operating systems have aggressive DNS caching. If changes don't appear to take effect, you may need to flush your DNS cache. This can be done by running ipconfig /flushdns in the Command Prompt.

## To the add the Minikube Ingress Addon
> minikube addons list
> minikube addons enable ingress

## whenever we want run or test the microservice architecture, we have run the below command
> minikube tunnel

# RabbitMQ
### Stateful-sets 
1. It is similar to the Deployment with few differences

2. It manages the deployment and scaling of a set of pods

3. Unlike the Deployment where the Pods are based on identical container spec, with the Stateful-Sets, each pods has a persistent identifier which it maintains for any rescheduling.

4. If a pod fails, then the persistent pod identifier makes it easier to identify and match the existing volumes to the new pod that replace any that have failed.
 - [Node ==> Pod ==> Container] ==> mount ==> [local disk volume]

5. In this project we will use one replica to achieve the "Competing Consumer Pattern" 

### [rabbitmq:3-management] | here management is required for the GraphQL user interface | we need to define two ports | [amqp] = [advanced message queuing protocol] to send messages to the queue

#### with [ClusterIP] ==> internal IP address and only accessible within the Cluster


## To get a Pod's status 

>  kubectl describe pod <pod_name>

## To DELETE  all Resources created within the Dir 

> kubectl delete -f ./

## To access the RabbitMQ manager from Browser we have to run
> minikube tunnel 

1. user: guest

## to read first 10 line

> cat file.py | head -n 10