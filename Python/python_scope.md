# 파이썬의 범위(Scope)

### Namespace : 식별자 기억하는 공간

1. Built-in
2. Global : .py file 안에
3. Enclosing
4. Local: 함수 안에 생성된 namespace

- Namespace 여러 개 존재, 같은 이름이 여러 곳에 존재할 수도 있다. 
- Local 부터 찾다가 Enclosing, Global, Built-in 순서로 찾음(scope 는 LEGB 순서)
-  예시: Local & Enclosing Namespace
```python
def func1():
    print('func1 start') #Enclosed

    def func2():
        print('func2 start') #Local
        print('func2 end')
        return
    func2()
    return

func1()
```
- 예시: Global에서 변수 찾기
```python
x = 'global'

def func1():

    def func2():
        print(x)
    func2()

func1() #global
```
- 예시 : Enclosed 에서 변수 찾기
```python
x = 'global'

def func1():
    x = 'enclosed'
    def func2():
        print(x)
    func2()

func1() #enclosed
```
- 예시 : Local 에서 변수 찾기
```python
x = 'global'

def func1():
    
    def func2():
        x = 'local'
        print(x)

    func2()

func1()  #local
```
- mutable 객체 이용(이후에 배움)
```python
my_list = [1,2,3,4]

def func1():
    my_list[1] = 5

func1()

print(my_list)
```
- Global and Nonlocal 예시
```python
x = 1

def func1():
    x = 2

    def func2():
        # global x (# 3 2 3)
        # nonlocal x (# 3 3 1)
        x =3
        print(x)
    func2()
    print(x)

func1()
print(x) # 3 2 1
```

