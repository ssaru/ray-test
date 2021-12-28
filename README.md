# ray-test
ray를 사용할 때, 몇몇 기능들에 대해서 어떻게 작동하는지, 테스트를 해봅니다.


1. [x] 함수를 ray actor argument로 전달하는게 가능한지?  
2. [x] 클래스를 ray actor argument로 전달하는게 가능한지  
3. [x] 상속받은 클래스를 ray actor로 사용할 수 있는지?  
4. [x] 가상 런타임(conda)를 ray cluster에서 사용할 수 있는지?  
5. [] ray.get일 때, 완료된 task가 리소스를 점유하고있는지? with placement group  

### Install
python은 3.7.x를 추천합니다.

```python
poetry install
```