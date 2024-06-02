import pika, os, sys, time 
from pymongo import MongoClient
import gridfs

# custom video to mp3 converter module
from convert import to_mp3

def main():
    client = MongoClient("host.minikube.internal", 27017)
    db_videos = client.videos
    db_mp3s = client.mp3s
    #gridfs 
    fs_videos = gridfs.GridFS(db_videos)
    fs_mp3s = gridfs.GridFS(db_mp3s)
    
    #rabbitmq connection 
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host="rabbitmq")
    )
    
    channel = connection.channel()
    
    # callback function to convert the video after consuming message from queue
    def callback(ch, method, properties, body):
        err = to_mp3.start(body, fs_videos, fs_mp3s, ch)
        if err:
            # back_nack = negative acknowledgement in case of failure | won't remove the message | it is required so that another process can consume the message
            # the delivery tag is used to uniquely identify the message that should be retried from queue of the channel by RabbitMQ
            ch.back_nack(delivery_tag=method.delivery_tag)
        else:
            ch.basic_ack(delivery_tag=method.delivery_tag)
    
    # config to consume messages from queue
    channel.basic_consume(
        queue=os.environ.get("VIDEO_QUEUE"),
        on_message_callback=callback
    )
    
    print("Waiting for messages... \n To exit press CTRL+C")
    
    # start listening on the channel to consume messages
    channel.start_consuming()
    
    if __name__ == "__main__":
        try:
            main()
        except KeyboardInterrupt:
            # graceful shutdown
            print("Interrupted")
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)