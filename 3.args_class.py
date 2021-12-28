import ray

class Dummy:
    def __init__(self, signature: int):
        self.signature = signature

@ray.remote
class Test:
    def __init__(self, rank: int, dummy_cls: Dummy):
        self.rank=rank
        self.dummy_cls = dummy_cls

    def say_rank(self):
        return self.rank

    def say_signature(self):
        return self.dummy_cls.signature

if __name__ == "__main__":
    """
    이전에 다른 Class를 argument로 전달할 때,
    Serialize 이슈로 에러가 발생했었는데, Ray 자체의 이슈는 아닌 것으로 보임
    """
    local_port = 10001
    host = f"ray://127.0.0.1:{local_port}"
    ray.init(host)

    num_worker = 5
    dummy_cls = Dummy(signature="test")
    actors = [Test.remote(rank=i, dummy_cls=dummy_cls) for i in range(num_worker)]
    processing_actors = [actors[i].say_signature.remote() for i in range(num_worker)]
    print(ray.get(processing_actors))

    ray.shutdown()