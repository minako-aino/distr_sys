import hazelcast

CLUSTER_NAME = "lab2"
QUEUE_NAME = "queue"

client = hazelcast.HazelcastClient(cluster_name=CLUSTER_NAME)
queue = client.get_queue(QUEUE_NAME).blocking()

try:
    while True:
        consumed_item = queue.take()
        print(f"Consumed {consumed_item}")

        if consumed_item == -1:
            queue.put(-1)
            break
finally:
    client.shutdown()
