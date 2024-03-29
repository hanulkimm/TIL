# Java 들어가기 전에

## 컴퓨터의 자료 표현
### 비트(Bit)
- Binary digit 
- 컴퓨터의 값을 저장할 수 있는 최소 단위
### 바이트 (Byte)
- 8 bits = 256 가지
- 정보의 최소 단위
### 2진수
- 2의 보수법
  1. 비트 반전
  2. 1 더해주기

## 자바 가상 머신(JVM)
- 자바 바이트코드를 실행할 수 있는 주체
- 자바 바이트 코드: 기계어와 유사하지만 기계어는 아님
- 자바 바이트 코드는 플랫폼에 독립적이며 모든 JVM은 자바 가상 머신 규격에 정의된 대로 자바 바이트 코드 실행
- C 프로그램과 비교: C프로그램은 컴파일 하면 기계어 출력, 운영체제에 맞게 컴파일 해줘야 함

![image](https://user-images.githubusercontent.com/122726684/228259792-9c90b5c4-90d2-47e0-8298-7b133cd06ee7.png)

# Java 기본
## main method
- 실행 명령인 java를 실행 시 가장 먼저 호출되는 부분
- Application의 시작: 특정 클래스의 main() 실행
  - main() 메소드 없다면 실행 불가
- 형태
![image](https://user-images.githubusercontent.com/122726684/228263113-d673bf05-ca38-45b5-bd19-454836ba431f.png)

## 주석 (Comment)
- // 내용: 해당 기호가 있는 위치 부터 그 줄 끝까지 주석 처리
- /* 내용 */: 해당 범위의 내용 주석 처리
- /** 내용 */: Documentation APIT를 위한 주석 처리

## 출력문
- print : 문자열 그대로 출력  
- println : 문자열 뒤에 개행 문자 더해줌("/n")
- printf:
  - %d: 정수
  - %f: 실수
  - %c: 문자
  - $s: 문자열

# 변수와 자료형
## 변수(Variable)
## 정의
- 데이터를 저장할 메모리의 위치를 나타내는 이름
- 변수의 타입 존재
- '='(할당 연산자)를 통해 CPU에게 연산작업을 의뢰
## 단위
- 0과 1을 표현하는 bit
- 8 bit = 1 byte
## 특징
- 대소문자 구분
- 공백 허용하지 않음
- 숫자로 시작할 수 없음

## 자료형
1. 기본 자료형
- 미리 정해진 크기의 메모리 크기 표현, 변수 자체에 값 저장
- 실수형: 근사값(정밀도 떨어짐), 15개의 유효 숫자

![image](https://user-images.githubusercontent.com/122726684/228858459-2cc4af19-c49a-41f0-93b0-6f10a33473d6.png)

2. 참조 자료형 
- 기본 자료형 8가지 외 모든 것

### 선언
- 자료형 변수명;
- ` int age;`, `String name;`
- String은 대표적 참조 자료형
### 저장(할당)
- 변수명 = 저장할 값;
- `age = 30;`, `name="하늘";`
### 초기화
- 자료형 변수명 = 저장할 값;
- `int age = 30;`

## 형 변환
- 자동(묵시적, 암묵적) 형변환이 가능한 방향
![image](https://user-images.githubusercontent.com/122726684/228860547-756e9f2b-8df1-48e8-8eb3-57769f1733ea.png)

1. 묵시적(암묵적) 형변환
- 범위가 넓은 데이터 형에 좁은 데이터 형 대입하는 것
- 즉, 작은 범위에서 큰 범위로 
- 예: `byte b = 100; int i=b`

2. 명시적 형변환
- 범위가 좁은 데이터 형에 넓은 데이터 형을 대입하는 것 
- 즉, 큰 범위에서 작은 범위로
- 예: `int i = 100; byte b = (byte) i;`

# 연산자
![image](https://user-images.githubusercontent.com/122726684/228861110-9bbb6e1f-5757-4a81-a779-40119829b64d.png)

## 단항 연산자
### 증감 연산자 ++, --
- 피연산자의 값을 1 증가, 감소 시킨다
- 전위형(prefix) ++1 : 먼저 변수의 값을 변화시키고 사용
- 후휘형(postfix) 1-- : 먼저 변수의 값 사용 후 변화
### 부호 연산자 +, -
- 숫자가 양수임을 표시
- 피연산자의 부호를 반대로 변경한 결과 반환 -
### 논리 부정 연산자 !
- 논리 값을 반전
- !true = false
### 비트 부정 연산자 ~
- 비트 값을 반전
- ~0 = 1, ~1 = 0
### 형 변환 연산자(type)
- 명시적 형 변환

## 산술 연산자
- 곱하기 *
- 나누기 /
- 나머지 %
- 더하기 +
- 빼기 -
- 정수와 정수의 연산은 정수, 정수와 실수의 연산은 실수
  - 둘 중 하나가 double이면 둘 다 double
  - 둘 중 하나가 float이면 둘 다 float
  - 둘 중 하나가 long이면 둘 다 long
  - 그렇지 않으면 둘 다 int로 계산

## 비교 연산자
### 대소 비교 연산
- `>, >=, <, <=`
### 동등 비교 연산
- `==, !=`
- String 변수 비교할 때는 equals() 사용
### 객체 타입 비교 연산
- instanceof

## 논리 연산자
- &&: 논리 곱(AND), 피연산자 모두가 TRUE일 때만 
- ! : 논리 부정(NOT), 피연산자의 결과를 반대로 바꾼다
- 효율적인 연산 가능

## 삼항 연산자
- 조건식 ? 식1 : 식2
- 조건식이 참일 경우, 식1 실행
- 조건식이 거짓일 경우, 식2 실행

## 복합 대입 연산자
- +=, -= , *=, /=


# 조건문
## IF - ELSE 문
- 조건식의 결과에 따라 블록 실행 여부가 결정
- 조건식: true/false 값을 산출할 수 있는 연산식 또는 boolean 타입 변수가 올 수 있음
- 조건식이 참일 경우 문장들을 실행하고 거짓일 경우 실행하지 않음
- 실행할 문장이 하나라면 중괄호 생략 가능
```java
if(조건식){
  실행할 문장1;
  실행할 문장2;
} else if {
  실행할 문장a;

} else {
  실행할 문장A;
}
```
## SWITCH 문
- 인자로 선택변수를 받아 변수의 값에 따라서 실행문이 결정
```java
switch(수식){
  case 값1:
    실행문 A;
    break;
  case 값2;
    실행문 B;
    break;
  default:
    실행문 C;
}
```

# 반복문
## For 문
```
for(초기화식;조건식;증감식;){
  반복 수행할 문장;
}
```
- 초기화는 반복문 시작될 때 한 번 실행
- 조건식이 False이면 반복문 종료
- 증감식은 반복문이 끝나면 실행
- 초기화식, 증감식은 ','을 이용하여 둘 이상 작성 가능
- 필요하지 않은 부분은 생략 가능
  - for(;;) 무한루프
- 반복횟수 알고 있을 때 유용

### 중첩 for 문
```
for (초기화식;조건식;증감식){
  for(초기화식;조건식;증감식){
    반복수행할 문장;
  }
}
```
- 예시
```java
outer: for (int i=0; i<3; i++){
  for (int j=0; j<3; j++){
    if (i==1) continue outer;
    System.out.println(i+","+j);
  }
}
```

## While 문
```
while(조건식){
  반복수행할 문장;
}
```
- 조건식이 true일 경우 반복
- 조건식 생략 불가능

### do while 문
```
do {
  반복수행할 문장;
} while (조건식);
```
- 블록 내용을 먼저 수행 후 조건식 판단
  - 최소 한번은 수행
- 조건식이 true일 경우 반복
- 조건식 생략 불가능

- 예시
```java
// While
import java.util.Scanner;

public class testwhile {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		while (num == 1) {
			System.out.println("블록을 실행합니다.");
			num = sc.nextInt();
		}
	}
}
// Do While
public class test_dowhile {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		do {
			System.out.println("블록을 실행합니다.");
			num = sc.nextInt();
		} while (num == 1);
	}

}

```

## break
- switch, while, do-while, for 문 블록에서 빠져나오기 위해 사용
- 반복문에 이름(라벨)을 붙여 한번에 빠져 나올 수 있음
## continue
- 반복문의 특정 지점에서 제어를 반복문의 처음으로 보냄
- 반복문에 이름(라벨)을 붙여 제어할 수 있음