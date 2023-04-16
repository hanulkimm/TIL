# 추상 클래스 (abstract class)

## 정의
- 조상 클래스에서 메서드의 선언부만 남기고 구현부는 ;(세미콜론)으로 대체
- 구현부가 없으므로 abstract 키워드를 메서드 선언부에 추가
- 객체를 생성할 수 없는 클래스라는 의미로 클래스 선언부에 abstract를 추가
```java
public abstract class Chef {
  String name;
  int age;
  String speciality;

  public void eat() {
    System.out.println("음식을 만든다");
  }
  public abstact void cook();
}
```
## 특징
- abstract 클래스는 상속 전용 클래스
- 클래스에 구현부가 없는 메서드가 있으므로 객체를 생성할 수 없음
- 상위 클래스 타입으로 자식을 참조할 수는 있음
- 조상 클래스에서 상속 받은 abstract 메서드를 재정의 하지 않는 경우 클래스 내부에 abstract 메서드가 있으므로 자식 클래스는 abstract 클래스가 되어야 함

## 사용 목적
- 구현의 강제를 통해 프로그램의 안정성 향상

![image](https://user-images.githubusercontent.com/122726684/232313452-d0a4de5a-d6ad-4cc0-9c28-479bed1cc2cb.png)

![image](https://user-images.githubusercontent.com/122726684/232313461-8adf04e6-9231-477c-a663-9e691e9192dc.png)