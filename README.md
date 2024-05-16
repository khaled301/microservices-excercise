# Microservices - Python

### Video to MP3 Conversion Processes
1. Client send the video upload request to API Gateway
2. Video gets saved in the database(MongoDB)
3. A notification is sent to the downstream services
3. Upload request sent to the message Queue (RabbitMQ)
4. Video to MP3 conversion service acquire the message and fetch the ID from the message
5. The converter service fetched the Video from the database
6. Convert the Video to MP3
7. Store the MP3 to the database
8. Send a successful conversion message to the queue
9. The queue let Notification service know about the conversion success
10. The client gets notified via email services about the successful conversion
11. The client then send another request to download the converted MP3 to the API Gateway with the Auth Token
12. API Gateway verify the request with help of an auth service
13. After the verification gets successful the API Gateway then request fetch the MP3 from the database and send it back to the client
14. The distributed system will be under a closed cluster and can't be accessed from outside world, open internet
15. Gateway service will be entry point of the overall application | received request from the client and will be communicate with the internal service to fulfill the request
16. we will define the functionality of the overall applications
17. auth service in the cluster will determine whom to access

### Install Docker for Windows

### Install K8s for Windows
```
> curl.exe -LO "https://dl.k8s.io/release/v1.30.0/bin/windows/amd64/kubectl.exe"

> curl.exe -LO "https://dl.k8s.io/v1.30.0/bin/windows/amd64/kubectl.exe.sha256"

> CertUtil -hashfile kubectl.exe SHA256

> type kubectl.exe.sha256

> $(Get-FileHash -Algorithm SHA256 .\kubectl.exe).Hash -eq $(Get-Content .\kubectl.exe.sha256)

> kubectl version --client

> kubectl version --client --output=yaml
```

### To setup k8s locally
https://minikube.sigs.k8s.io/docs/start/

```
>> New-Item -Path 'c:\' -Name 'minikube' -ItemType Directory -Force

>> Invoke-WebRequest -OutFile 'c:\minikube\minikube.exe' -Uri 'https://github.com/kubernetes/minikube/releases/latest/download/minikube-windows-amd64.exe' -UseBasicParsing

>> $oldPath = [Environment]::GetEnvironmentVariable('Path', [EnvironmentVariableTarget]::Machine)
if ($oldPath.Split(';') -inotcontains 'C:\minikube'){
  [Environment]::SetEnvironmentVariable('Path', $('{0};C:\minikube' -f $oldPath), [EnvironmentVariableTarget]::Machine)
}
```

### K9s - Kubernetes CLI To Manage Your Clusters In Style!

https://github.com/derailed/k9s

K9s provides a terminal UI to interact with your Kubernetes clusters.
The aim of this project is to make it easier to navigate, observe and manage
your applications in the wild. K9s continually watches Kubernetes
for changes and offers subsequent commands to interact with your observed resources.


### Download and install Python

https://www.python.org/

### Download and install MySQL

https://www.mysql.com/downloads/

```
mysql -u<user_name> -p<password>
```