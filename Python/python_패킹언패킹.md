# 패킹과 언패킹

### 패킹/언패킹 연산자 *
- 모든 시퀀스형은 패킹/언패킹 연산자 * 사용하여 패킹/언패킹 가능
- 패킹: 대입문의 좌변 변수에 위치하여 우변의 객체 수가 더 많을경우 남은 항목들을 * 표시된 변수에 리스트로 대입
```python
x, *y = 1,2,3,4
print(y) # [2,3,4]
print(type(y)) # list
```
- 언패킹: 튜플 형태로 대입
```python
def my_sum(a,b,c):
    return a + b + c
numbers = [1,2,3]
my_sum(*numbers)
```
- 가변인자(*args): 몇 개의 positional argument를 받을 지 모르는 함수를 정의할 때 유용
```python
def test(*values):
    for value in values:
        print(value)

test(1,2)
```
```python
def my_sum(a,*args): #꼭 한 개 이상의 insert 받아야 할 때
    result = 0
    for value in args:
        result += value
    return result
print(my_sum(1,2,3))
```
- 가변 키워드 인자(**kwrags): 딕셔너리로 묶여 처리된다
```python
def result(**kwargs):
    print(kwargs)

result(name = 'hanul', age = 24)
```
- 예시: 가변인자와 가변 키워드 인자 동시 사용 
```python
def result(*args,**kwargs):
    print(args,kwargs)

result(1,2,3, name = 'hanul', age = 24)
```