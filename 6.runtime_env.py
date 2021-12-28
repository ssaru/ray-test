import ray
import pandas as pd
import lightgbm

@ray.remote
class Test:
    def __init__(self, rank):
        self.rank=rank
        self.classifier = lightgbm.LGBMClassifier()

    def classifier_info(self):
        return dir(self.classifier)

if __name__ == "__main__":
    # # Using Serial Code. @ray.remote decorator should be removed
    # test_cls = Test(rank=0)
    # print(test_cls.classifier_info())
    # exit()

    local_port = 10001
    host = f"ray://127.0.0.1:{local_port}"

    # Not using ray runtime. it will raise Error
    # such as ModuleNotFoundError: No module named 'lightgbm'
    # ray.init(host)

    # num_worker = 5
    # actors = [Test.remote(rank=i) for i in range(num_worker)]
    # processing_actors = [actors[i].classifier_info.remote() for i in range(num_worker)]
    # print(ray.get(processing_actors))

    # ray.shutdown()

    # Using ray runtime.
    ray.init(host, runtime_env={"pip": ["lightgbm==3.3.1"]},)

    num_worker = 5
    actors = [Test.remote(rank=i) for i in range(num_worker)]
    processing_actors = [actors[i].classifier_info.remote() for i in range(num_worker)]
    print(ray.get(processing_actors))

    ray.shutdown()
