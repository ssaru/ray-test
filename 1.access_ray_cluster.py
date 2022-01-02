import ray

"""
Setting Ray Cluster in kubernetes using docker-desktop
refer: https://docs.ray.io/en/latest/cluster/kubernetes.html

NOTE.
Recommend python 3.7.x
ray experimentally support python 3.8.x 

TODO.
should be fill in resources value in `values.yaml`
HEAD: rayResources: {"CPU":0}
WORKER: rayResources: {"CPU": 1, "memory": 512 * 1024 * 1024}

helm chart install/uninstall을 반복하면, container가 잘 생성되지 않는 이슈가 있음
helm install 시에 command 명령을 조금씩 바꿔주면되는데,,,
캐시가 있나?....
"""
local_port = 10001
host = f"ray://127.0.0.1:{local_port}"
ray.init(host)

print("Hello Ray")

ray.shutdown()