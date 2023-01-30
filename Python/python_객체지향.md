# 객체 지향 프로그래밍

## OOP 기초
- 객체 지향 프로그래밍이란?   
  프로그램을 여러 개의 독립된 객체들과 그 객체 간의 상호작용으로 파악하는 프로그래밍 방법
- 하나의 객체에는 데이터와 이를 활용하는 여러 함수들이 존재, 함수들을 메서드라 부른다.
- 절차지향 프로그래밍에 비해 효율적임
### 장점
- 재사용 가능
- 객체는 데이터와 행동이 독립적이라 개발자가 내부 구조를 몰라도 다른 객체와 조립하면서 개발이 가능
- 객체 단위로 모듈화시켜 개발할 수 있어서 대규모 소프트웨어 개발 가능
- 즉, 개발이 용이하고 유지 보수가 편의하고 신뢰성을 바탕으로 생산성이 대폭 증가한다
### 단점
- 설계 시 많은 노력과 시간이 필요하다
- 실행 속도가 상대적으로 느림

### 객체
- 클래스에서 정의한 것을 토대로 메모리(실제 저장공간)에 할당된 것
- 속성과 행동으로 구성된 모든 것
- 파이썬은 모든 것이 객체, 모든 데이터 타입은 모두 클래스
### 인스턴스
- 클래스로 만든 객체를 인스턴스라고 함

## OOP 문법 
 
### 기본 문법
- 클래스 정의: `class Myclass:`
- 인스턴스 생성 :  `my_instance = Myclass()`
- 메서드 호출 : `my_instance.my_method()`
- 속성 접근 : `my_instance.my_attribute()`

### 객체 비교하기
- '==' : 변수가 참조하는 객체가 동등한(내용이 같은)(equal) 경우 True
- 'is' :  두 변수가 동일한(identical) 객체를 가리키는 경우 True
### 속성
- 클래수 변수 / 인스턴스 변수 존재
```python
class Person:
    population = 100 # class 변수

    def __init__(self, name):
        self.name = name # 인스턴스 변수
person1 = Person('하늘')
print(person1.name) #하늘
```


### **인스턴스 변수**
- 인스턴스가 개인적으로 가지고 있는 속성, 각 인스턴스들의 고유한 변수
- 생성자 메서드에서 self.name 으로 정의
```python
class Person:
    def __init__(self,name): # 인스턴스 변수 정의
        self.name = name
john = Person('john') # 인스턴스 변수 접근 및 할당
print(john.name) # john
john.name = 'John Kim
print(john.name) # John Kim
```

### **클래스 변수**
- 한 클래스의 모든 인스터스가 공유하는 값
- classname.name 으로 접근 및 할당
```python
class Circle():
    pi = 3.14

    def __init__(self,r):
        self.r = r
c1= Circle(5)
print(Circle.pi) # 5
print(c1.pi) # 5
```
- 클래스 변수 활용해서 사용자 수 계산하기
```python
class Person:
    count = 0

    def __init__(self,name):
        self.name = name
        Person.count += 1
person1 = Person('김하늘')
person2= Person('김떙땡')

print(Person.count) # 2
```



## OOP 메서드

### 메서드: 특정 데이터 타입/클래스의 객체 공통적으로 적용 가능한 함수
```python
class Person:

    def talk(self): # 인스턴스 메서드
        print('hi')
    def eat(self, food): # 인스턴스 메서드
        print(f'{food}를 냠냠')

person1.Person()
person1.talk() # hi
person1.eat('피자') # 피자를 냠냠
person1.eat('치킨') #  치킨을 냠냠
```
### 메서드 종류:
- 인스턴스 메서드: 가장 흔함, 인스턴스 변수를 사용하는 함수 만들고 싶을 때 활용
- 클래스 메서드: 클래스 변수를 가지고 활용할 때(인스턴스 상관 무)
- 정적 메서드: 인스턴스와 클래스 활용 할 필요 없음

## 인스턴스 메서드
- 인스턴스 변수 사용하거나 인스턴스 변수에 값을 설정하는 메서드
- 클래스 내부에 정의되는 메서드의 기본
- 호출 시, 첫번째 인자로 self이 자동으로 전달됨

### Self
- 인스턴스 자기자신
- 인스턴스 메서드는 호출 시 첫번째 인자로 자신이 전달되게 설계
    - 매개변수 이름으로 self를 첫번째 인자로 정의


### 생성자 메서드
- 인스턴드 객체 생성 시 자동으로 호출되는 메서드
- 인스턴트 변수들의 초기값 설정
```python
class Person:
    def __init__(self):
        print('instance 생성')
person1 = Person() # instance 생성
```

### 매직메서드 
- `__str__(self)` : 객체를 문자열로 표현하면 어떻게 표현할 지를 지정, print함수에서 객체를 출력하면 자동으로 호출되는 메서드
  - `__gt__`: 부등호 연산자
- 예시
```python
class Circle:
    def __init__(self,r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r
    
    def __str__(self):
        return f'원 radius : {self.r}'

    def __gt__(self,other):
        return self.r > other.r
c1 = Circle(10)
c2 = Circle(1)

print(c1) # 원 radis : 10
print(c1,c2) # 원 radius : 10 원 radius : 1
print(c1>c2) # True
```

## 클래스 메서드
- `@classmethod` 데코레이터 사용하여 정의 
- 호출 시, 첫번째 인자로 클래스(cls)가 전달됨
```python
class Myclass:

    @classmethod
    def class_method(cls, *args)
```
- 클래스 메서드 예시
```python
class Person:
    count = 0
    def __init__(self, name):
        self.name = name
        Person.count += 1
    @classmethod
    def number_of_popoulation(cls):
        print(f'인수수는 {count}입니다.')
person1 = Person('김하늘')
person2= Person('김떙땡')

person1.number_of_popoulation() # 인구수는 2입니다.
person2.number_of_popoulation() # 인구수는 2입니다.
```

