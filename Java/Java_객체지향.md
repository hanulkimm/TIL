# 객체지향 프로그래밍

## 개념
- 클래스: 객체를 만드는 설계도(blueprint, template)
- 인스턴스: 클래스를 통해 생성된 객체
- 특징: 추상화, 다형성, 상속, 캡슐화
- 장점: 모듈화된 프로그래밍, 재사용성이 높음


## 클래스
- 변수와 함수를 묶어서 만든 사용자 정의 <자료형>
- 객체를 생성하는 틀
- 프로그래밍 목적에 따라 어떤 특징(속성, 동작)을 가지는 지 결정
- 클래스를 통해 생성된 객체는 인스턴스

### 구성
- 속성: 필드, 변수, 데이터
- 동작: 메서드
- 생성자: 객체를 생성할 때
- 중첩 클래스
```java
[접근제한자][활용제한자] class 클래스명 {
  속성 정의(필드, 변수)
  기능 정의 (메서드)
  생성자
}
```
- 예시:
```java
public class Person {
  String name;
  int age;

  public void eat( ){
  }
  // 생성자 생략하면 자동으로 만들어줌
  public Person(){
  } 
}

```

## 변수
### 클래스 변수(class variable)
- 클래스 영역 선언(static 키워드)
- 모든 인스턴스가 공유함
### 인스턴스 변수
- 인스턴스 별로 고유하게 생성됨
### 지역 변수
- 클래스 영역 이외에 사용(메서드, 생성자 등..)
```java
// Person.java
public class Person{
  // 클래스 변수
  static String species = "호모 사피엔스";
  // 인스턴스 변수
  String name;
  int age;
  // 메서드
  public void eat(){
    String dish = "치킨";
  }
}
// PersonTest.java
public class PersonTest {
  public static void main(String[] args) {
    Person p1 = new Person();
    System.out.println(p1.species);
    System.out.println(Person.species);
    // 호모 사피엔스 
    // 호모 사피엔스 

  }
}
```

## 메서드 (Method)
- 특정한 직업을 수행하는 문장들을 묶어서 이름을 붙인 것
- 객체가 할 수 있는 행동 정의
- 메소드의 이름은 소문자로 시작하는 것이 관례
- 예시:
```java
public static void main(String[] args){}
```
### 메서드 오버로딩
- 이름이 같고 매개변수가 다른 메서드를 여러 개 정의하는 것
- 중복 코드에 대한 효율적 관리 가능
- 파라미터의 개수, 순서, 타입이 달라져야 함
- 리턴 타입이 다른 것은 의미가 없음
- 예시:
```java
	public int add(int a, int b) {
		return a+b;
	}
	public double add(double a, double b) {
		return a+b;
	}
  public void eat() {
  System.out.println("식사를 합니다");
		
	}
	public void eat(String dish) {
		System.out.println(dish+ "를 먹습니다");
	}
	
```

## 생성자
- new 키워드와 함께 호출하여 객체 생성
- 클래스명과 동일(대,소문자)
- 결과형 리턴값을 갖지 않음, 반환타입이 없음
- 객체가 생성될 때 반드시 하나의 생성자 호출
- 멤버필드 초기화에 주로 사용
하나의 클래스 내부에 생성자가 하나도 없으면 자동적으로 default생성자가 있는 것으로 인지
- 매개변수의 개수가 다르거나 자료형이 다른 여러 개의 생성자가 있을 수 있음
- 생성자의 첫번째 라인으로 this()생성자를 사용하여 또 다른 생성자를 하나 호출 가능

### 기본(디폴트 생성자)
- 클래스 내에 생성자가 하나도 정의되어 있지 않을 경우 JVM이 자동으로 제공하는 생성자
- 형태: 매개변수가 없는 형태, 클래스명() {}

### 파라미터가 있는 생성자
- 생성자의 목적이 필드 초기화
- 생성자 호출 시 값을 넘겨줘야 함
- 해당 생성자를 작성하면 JVM에서 기본 생성자를 추가하지 않음
- 예시:
```java
// Person.java
public class Person {
  // 기본 생성자
  public Person(){
    this("홍길동", 30);
  }
  // 파라미터 있는 생성자
  public Person(String name, int age){
    this.name = name;
    this.age = age;
  }
}

// PersonTest.java
public class PersonTest {
  Person p1 = new Person("김하늘", 24);
	Person p2 = new Person();
}
```

### 생성자 오버로딩
- 클래스 내에 메소드 이름이 같고 매개변수의 타입 또는 개수가 다른 것

![image](https://user-images.githubusercontent.com/122726684/230418899-99785051-fb5d-4055-90f9-bc52c0b5cee1.png)

### this
- 객체 자신을 가르키는 참조 변수
- 지역변수(매개변수)와 필드의 이름이 동일한경우, 필드임을 식별할 수 있게 함
- 객체에 대한 참조이므로 static 영역에서 this 사용 불가
- 활용
  - this.멤버변수
  - this([인자값]..): 생성자 호출
  - this 생성자: 생성자 내에서만 호출 가능, 생성자 내 첫번째 구문에 위치해야함
- 예시:
```java
	public Person() {
		this("홍길동", 30);
	}
	
	public Person(String name, int age){
		// this
		this.name = name;
		this.age = age;
	}
	public void sleep() {
		System.out.println("잠을 잡니다.");
	}
	
	public void eat() {
		System.out.println("식사를 합니다");
		this.sleep();
  }
```

## 접근 제한자

### 패키지
- 클래스 관리 위해 패키지 사용
- 클래스와 관련 있는 인터페이스들을 모아두기 위한 이름 공간
- 패키지의 구분은 .(dot)연산자 이용
- 시중에 나와 있는 패키지들과 구분하게 지어야 함
  - 일반적으로 소속이나 회사의 도메일 사용함
  - 예시: `도메인.project_name.modele_name`

### 임포트
- 다른 패키지에 있는 클래스를 사용하기 위해서 import 과정이 필요
- import 선언 시, import 키워드 뒤에 package 이름과 클래스 이름 모두 입력하거나 패키지의 모든 클래스를 포함할 때는 '*'를 사용하기도 함
- `import package_name.class_name;`
- `import package_name.*;`

## 접근 제한자
- 접근 허용 범위를 지정하는 역할의 키워드

### 종류
- public: 모든 위치에서 접근 가능
- protected: 같은 패키지에서 접근 가능, 다른 패키지 접근 불가능, 다른 패키지와 상속 관계있을 경우 접근 가능
- (default): 같은 패키지에서만 접근 허용
- private: 자신 클래스에만 접근 허용

- 그외: 
  - static: 클래스 레벨의 요소 설정
  - final: 요소를 더 이상 수정할 수 없게 함

- 클래스(외부) 사용 가능: public, default
- 내부 클래스, 멤버변수, 메서드 사용 가능: 4가지 모두 가능

![image](https://user-images.githubusercontent.com/122726684/230717834-596087d9-1556-48df-805b-0b3fa88d0b81.png)

![image](https://user-images.githubusercontent.com/122726684/230719380-e0a18ee0-b976-44c7-918f-4313d9b123b3.png)

### 접근자(getter)/ 설정자(setter)
- 클래스에서 선언된 변수 중 접근제한에 의해 접근할 수 없는 변수의 경우, 다른 클래스에서 접근할 수 없기 때문에 접근하기 위한 메서드를 public으로 선언하여 사용

![image](https://user-images.githubusercontent.com/122726684/230719927-b0b8555a-48a6-4454-bb35-e0c9126e86ed.png)

```java
// PersonTest.java
public class PersonTest {
	public static void main(String[] args) {
		Person p1 = new Person();
		p1.setName("김하늘"); //public method이니까 접근 가능
		p1.setAge(24);
		System.out.println(p1.getName());
		System.out.println(p1.getAge());
	}
}
```

### 싱글턴 패턴(Singleton Pattern)
- 생성자가 여러 차례 호출되더라도 실제로 생성되는 객체는 하나이고 최초 생성 이후에 호출된 생성자는 최초즤 생성자가 생성한 객체를 리턴
```java
// Person.java
public class Person{
  private static Person instance = new Person();
  private Person(){
    this.name = "김하늘";
    this.age = 24;
  }
  public static Person getInstance() {
    return instance;
  }
}

// PersonTest.java
public class PersonTest(){
  public static void main(String[] args) {
    Person p1 = getInstance();
    System.out.println(p1.getName());
    // 김하늘
		System.out.println(p1.getAge());
    // 24
  }
}
```
## JVM 메모리 구조
![image](https://user-images.githubusercontent.com/122726684/230754507-fdb9e287-cebb-4956-938d-4267eb8c3fd9.png)

## static 특징
1. 로딩 시점:
- static: 클래스 로딩 시
- non-static: 객체 생성 시
2. 메모리상의 차이
- static: 클래스당 하나의 메모리 공간만 할당
- non-static: 인스턴스 당 메모리가 별도로 할당
3. 문법적 특징
- static: 클래스 이름으로 접근
- non-static: 객체 생성 후 접근
```java
public class Person{
  static int age;
  String name;
  int grade;
}

public class PersonTest {
  public static void main(String[] args) {
    // 클래스 이름으로 접근
    Person.age;
    // 객체 생성 후 접근
    Person p1 = new Person();
    p1.name="KIM"
    
  }
}   
```

4. static 영역에서는 non-static 영역 직접 접근 불가능
5. non-static 영역에서는 static 영역에 대한 접근이 가능

