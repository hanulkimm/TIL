# Python 함수

### 함수 정의
``` python
def function_name(paramter):
    # code block
    return return_value
```
- Return문 통해, 값 반환하고 함수는 종료
- Return문이 없으면, None을 반환

### Print 와 Return의 차이 구분하기!
```python
  def print(x,y):
    if x < y:
        print(y)
    else:
        print(x)
```
   print(2,3) 하면 결과: 3 None
```python
 def print(x,y):
    if x < y:
        return(y)
    else:
        return(x)
```
print(2,3) 하면 결과: 3

## 내장 함수

**Map**
```python
map(function,iterable)
```
- iterable의 모든 요소에 함수 적용
- map object 으로 변환, 형변환 필요함
    - 입력한 개수 만큼의 변수가 있다면 형변환 필요없음

**Filter**
```python
filter(function,iterable)
```
- iterable의 모든 요소에 function 적용하고 결과가 True인 것들만 반환
- 리스트 형변환 통해 결과 확인 할 수 있음
- 예시: 홀수 숫자 출력
```python
def odd(n):
    return n % 2
numbers = [1,2,3]
result = filter(odd,numbers)
print(type(result)) # filter
print(list(result)) # list 로 형변환
```
**Zip**
```python
zip(*iterables)
```
- 복수의 iterable을 모아 tuple을 원소로 하는 zip object 반환
- 예시
```python
name_list = ['kim','lee','park']
age_list = [19,17,18]
print(list(zip(name_list,age_list))) # 형변환

for name,age in zip(name_list,age_list):
    print(name,age) 
```

**Lambda**
```python
lambda 매개변수 : 표현식
```
- 예시
```python
result = map(lambda x : x* 10,[1,2,3])
print(list(result)) #[10,20,30]
```

**재귀함수**
- 자기 자신을 호출하는 함수
- 1개 이상의 base case가 존재함, 수렴하도록 작성해야 한다
- 예시: Factorial
```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
print(factorial(4))
```