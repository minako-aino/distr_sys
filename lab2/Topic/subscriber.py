import hazelcast
from datetime import datetime


def message_listener(event):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    print(f"Received: {event.message} at {current_time}")


client = hazelcast.HazelcastClient(cluster_name="lab2")
hz_topic = client.get_topic("lab2").blocking()
hz_topic.add_listener(message_listener)

print("Listening for messages...")
input("Press Enter to stop...\n")

client.shutdown()