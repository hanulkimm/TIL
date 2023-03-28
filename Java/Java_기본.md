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