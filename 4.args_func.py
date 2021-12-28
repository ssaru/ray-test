import ray

def say_hello():
    return "Hello"

@ray.remote
class Test:
    def __init__(self, rank: int, func: object):
        self.rank=rank
        self.func = func

    def say_rank(self):
        return self.rank

    def call_func(self):
        return self.func()

if __name__ == "__main__":
    local_port = 10001
    host = f"ray://127.0.0.1:{local_port}"
    ray.init(host)

    num_worker = 5
    actors = [Test.remote(rank=i, func=say_hello) for i in range(num_worker)]
    processing_actors = [actors[i].call_func.remote() for i in range(num_worker)]
    print(ray.get(processing_actors))

    ray.shutdown()