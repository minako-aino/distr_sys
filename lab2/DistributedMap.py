import hazelcast

client = hazelcast.HazelcastClient(cluster_name="lab2")
hz_map = client.get_map("lab2").blocking()

for i in range(1000):
    hz_map.put(i, f"value{i}")

client.shutdown()