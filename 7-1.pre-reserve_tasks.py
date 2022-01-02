import ray
import time

from ray.util.placement_group import (
    placement_group,
    placement_group_table,
    remove_placement_group
)

@ray.remote(num_cpus=1, memory=512 * 1024 * 1024)
def sleep_tasks(rank: int):
    if rank == 0:
        time.sleep(1000)

    return "Hello Ray!"

if __name__ == "__main__":
    
    local_port = 10001
    host = f"ray://127.0.0.1:{local_port}"
    ray.init(host)

    # Ray example cluster has only two ray workers
    # default resource setting are CPU: 1, Memory: 512Mi
    # So, resource is fully reserved when using placement group below..
    pg = placement_group([{"CPU": 1, "memory": 512 * 1024 * 1024}, 
                          {"CPU": 1, "memory": 512 * 1024 * 1024}])
    ray.get(pg.ready())

    num_worker = 2
    futures = [sleep_tasks.options(placement_group=pg).remote(rank=i) for i in range(num_worker)]
    print(ray.get(futures))

    ray.shutdown()