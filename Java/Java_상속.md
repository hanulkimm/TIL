# 상속 Inheritance
## 개념
- 어떤 클래스의 특성을 그대로 갖는 새로운 클래스를 정의한 것

![image](https://user-images.githubusercontent.com/122726684/231786465-1c5f59e0-c79a-4ad4-b893-48800cf604a9.png)

```java
public class Person {
  String name;
  int age;

  public void eat() {
    System.out.println("음식을 먹는다");
  }
}

public class Student extends Person {
  String major;

  public void study() {
    System.out.println("공부를 한다.");
  }

}
```

## 특징
1. 확장성, 재사용성
- 부모의 생성자와 초기화 블록은 상속 안됨
2. 클래스 선언 시 extends 키워드 명시
- 다중 상속은 안됨, 단일 상속 지원
3. 자식 클래스는 부모 클래스의 멤버 변수, 메서드를 사용할 수 있음
- 접근 제한자에 따라 사용 여부 바뀜
4. Object 클래스는 모든 클래스의 조상 클래스
- 별도의 extends 선언이 없는 클래스는 extends Object 가 생략
5. super 키워드
- super를 통해 조상 클래스의 생성자 호출
6. 오버라이딩 (재정의, overriding)
- 상위 클래스에 선언된 메서드를 자식 클래스에서 재정의 하는 것
- 메서드의 이름, 반환형, 매개변수(타입,개수,순서) 동일해야 함
- 하위 클래스의 접근제어자 범위가 상위 클래스보다 크거나 같아야 함
- 메서드 오버로딩과 혼동 하지 말기!!!!!!!
```java
// Person class
public class Person {
  String name;
  int age;

  public Person(String name, int age) {
    this.name = name;
    this.age = age;
  }
  public void eat() {
    System.out.println("음식을 먹는다");
  }
}

// Student class
public class Student extends Person {
  String major;

  public Student(String name, int age, String major) {
    super(name, age);
    this.major = major;
  }
  public void study() {
    System.out.println("공부를 한다.");
  }

  @Override
  public void eat() {
    System.out.println("지식을 먹는다");
  }
}

Student st = new Student("김하늘", 24, "통계")
st.study();
// 공부를 한다
// 지식을 먹는다
```

## Object Class
![image](https://user-images.githubusercontent.com/122726684/231791330-16244458-89f7-408d-932c-c387d4036b39.png)
- 가장 최상위 클래스로 모든 클래스의 조상
- Object의 멤버는 모든 클래스의 멤버
- 주소 값이 아닌 내용이 궁금할 때:
```java
@Override
public String toString() {
  return "Student [name=" + name + ", age=" + age + ", major=" + major + "]";
}
```
## equals 메서드
- 두 객체가 같은지 비교하는 메서드(주소 값 기준)
```java
public boolean equals(Object obj) {
  return (this==obj);
}
```
- 두 객체의 내용 비교할 때는 equals 재정의

## hashcode
- 객체의 해시 코드: 시스템에서 객체를 구별하기 위해 사용되는 정수값
- equals 메서드를 재정의 할 때는 반드시 hashCode도 재정의 할 것
- 미리 작성된 String이나 Number등에서 재정의 된 hashcode 활용 권장

![image](https://user-images.githubusercontent.com/122726684/231793539-218b16df-ab79-4ff0-85fa-6fd15e41773c.png)

## final
- 해당 선언이 최종 상태, 결코 수정 될 수 없음
- final 클래스: 상속 금지
- final 메서드: overriding 금지
- final 변수: 더 이상 값을 바꿀 수 없음 상수화
