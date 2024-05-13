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