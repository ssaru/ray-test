import ray

"""
Setting Ray Cluster in kubernetes using docker-desktop
refer: https://docs.ray.io/en/latest/cluster/kubernetes.html

NOTE.
Recommend python 3.7.x
ray experimentally support python 3.8.x 
"""
local_port = 10001
host = f"ray://127.0.0.1:{local_port}"
ray.init(host)

print("Hello Ray")

ray.shutdown()