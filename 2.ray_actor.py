import ray

@ray.remote
class Test:
    def __init__(self, rank):
        self.rank=rank

    def say_rank(self):
        return self.rank

if __name__ == "__main__":
    local_port = 10001
    host = f"ray://127.0.0.1:{local_port}"
    ray.init(host)

    num_worker = 5
    actors = [Test.remote(rank=i) for i in range(num_worker)]
    processing_actors = [actors[i].say_rank.remote() for i in range(num_worker)]
    print(ray.get(processing_actors))

    ray.shutdown()