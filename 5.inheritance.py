import ray

class _BaseTest:
    def __init__(self, rank: int):
        self.rank = rank

@ray.remote
class Test(_BaseTest):
    def __init__(self, rank: int):
        super().__init__(rank=rank)

    def say_rank(self):
        return self.rank

if __name__ == "__main__":
    """
    이전에 Class 상속된 Actor를 사용했을 때,
    Serialize 이슈로 에러가 발생했었는데, Ray 자체의 이슈는 아닌 것으로 보임
    """
    local_port = 10001
    host = f"ray://127.0.0.1:{local_port}"
    ray.init(host)

    num_worker = 5
    actors = [Test.remote(rank=i) for i in range(num_worker)]
    processing_actors = [actors[i].say_rank.remote() for i in range(num_worker)]
    print(ray.get(processing_actors))

    ray.shutdown()