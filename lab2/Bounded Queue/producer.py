import hazelcast

CLUSTER_NAME = "lab2"
QUEUE_NAME = "queue"

client = hazelcast.HazelcastClient(cluster_name=CLUSTER_NAME)

try:
    queue = client.get_queue(QUEUE_NAME).blocking()
    for i in range(100):
        queue.put(i)
        print(f"Producing {i}")
    queue.put(-1)
    print("Producer finished")

finally:
    client.shutdown()
