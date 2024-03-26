import hazelcast
import time

client = hazelcast.HazelcastClient(cluster_name="lab2")
hz_topic = client.get_topic("lab2").blocking()

for i in range(1, 101):
    hz_topic.publish(f"Message {i}")
    print(f"Published: Message {i}")
    time.sleep(1)

client.shutdown()