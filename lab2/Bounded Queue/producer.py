import hazelcast

client = hazelcast.HazelcastClient(cluster_name="lab2")
queue = client.get_queue("queue").blocking()

for i in range(100):
    queue.put(i)
    print("Producing " + str(i))
queue.put(-1)
print("Producer finished")
client.shutdown()

"""import hazelcast


client = hazelcast.HazelcastClient(cluster_name="lab2")

queue = client.get_queue("queue").blocking()
print('starting stuff')
for i in range(1, 101):
    queue.put(i)
    print("Producing " + str(i))
queue.put(-1)
print("Producer finished")

client.shutdown()
"""