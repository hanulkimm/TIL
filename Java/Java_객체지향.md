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