# JavaScript 시작하기

## JavaScript 개념
- JavaScript는 클라이언트 측 웹(브라우저)에서 실행
  - 웹 페이지가 이벤트 발생 시 어떻게 작동하는 지 디자인/프로그래밍 
  - 웹 페이지 동작을 제어하는 데 널리 사용
- Web 기술의 기반이 되는 언어
  - HTML 문서의 콘텐츠를 동적으로 변경할 수 있는 언어
  - Web이라는 공간에서 채팅, 게임 등 다양한 동작을 할 수 있게 된 기반

## JavaScript Engine
- JavaScript 코드를 실행하는 프로그램 또는 인터프리터
- 여러 목적으로 JavaScript 엔젠을 사용하지만 대체적으로 웹 브라우저에서 사용(대체로 내장)

### 웹 브라우저 역할
- URL 통해 Web(WWWW) 탐색
- HTML/CSS/JavaScript를 이해한 뒤 해석해서 사용자에게 하나의 화면으로 보여줌
- 웹 서비스 이용 시 클라이언트의 역할을 함
- 웹 페이지 코드를 이해하고 보여주는 역할을 함

### JavaScript Engine
- 각 브라우저마다 자체 JavaScript Engine을 개발, 사용하고 있음
- 브라우저 외에 활용: Node.js

## JavaScript 실행 환경 구성
1. HTML 파일 포함시키기
- 반드시 닫는 body 태그 위에 작성
```html
<body>
  <script>
    console.log("Hello JavaScript")
  </script>
</body>
```
2. 외부 JavaScript 파일 사용하기
```js
// hello.js
console.log("Hello JavaScript")
```
```html
<script type="text/javascript" scr="hello.js"></script>
```
3. Web Browser에서 바로 입력하기

- 특별하게 웹 브라우저에서 바로 실행할 수 있는 javaScript 문법들은 VanillaScript라고 부름

# 기초 문법
## 변수와 식별자
### 식별자
- 변수를 구분할 수 있는 변수명
- 문자, 달러, 또는 밑줄로 시작
- 대소문자 구문, 클래스명 외에는 모두 소문자로 시작
- 예약어 사용 불가능
### Case
- 카멜 케이스(camelCase) : 변수, 객체, 함수에 사용

![image](https://user-images.githubusercontent.com/122726684/232644734-fd92656b-4305-4d60-b583-5cb3d4da6751.png)

- 파스칼 케이스(PascalCase) : 클래스, 생성자에 사용

![image](https://user-images.githubusercontent.com/122726684/232644753-bceec389-be5a-45e5-943b-a536791d38a5.png)

- 대문자 스네이크 케이스(SNAKE_CASE) : 상수(constant)에 사용
  - 상수: 개발자의 의도와 상관없이 변경될 가능성이 없는 값
  
![image](https://user-images.githubusercontent.com/122726684/232644772-de1ab360-a5a4-4e93-9270-d7f8fcd41c97.png)


## 변수 선언 키워드
### 1. let
- 블록 스코프 지역 변수를 선언
- 선언과 동시에 원하는 값으로 초기화
- 재할당 가능 & 재선언 불가능

![image](https://user-images.githubusercontent.com/122726684/232644981-67586528-5193-4305-a101-599012b6983e.png)  

### 2. const
- 블록 스코프 읽기 전용 상수를 선언
- 선언시 반드시 초기값 설정해야 함, 이후에 값 변경 불가능
- 재할당 불가능, 재선언 불가능

![image](https://user-images.githubusercontent.com/122726684/232645001-9ca52980-d603-473c-9be6-1bcb4315e7f4.png)

### 3. var
- 재할당 가능, 재선언 가능
- ES6 이전에 변수를 선언할 때 사용되던 ㅋ워드
- ES6 이후에는 var 대신 const 와 let 사용 권장
- 함수 스코프를 가짐
- 변수 선언 시 var, const, let 키워드 중 하나를 사용하지 않으면 자동으로 var 로 선언
- 호이스팅 되는 특성으로 예기치 못한 문제 발생 가능
  - 호이스팅: 변수를 선언 이전에 참조할 수 있는 현상

## 선언, 할당, 초기화
### 선언 
- 변수를 생성하는 행위 또는 시점
### 할당
- 선언된 변수에 값을 저장하는 행위 또는 시점
### 초기화
- 선언된 변수에 처음으로 값을 저장하는 행위 또는 시점

```js
let a; // 선언
console.log(a) // undefined

a = 1 // 할당
console.log(a) // 1

let a = 1 // 선언 + 할당
console.lon(a) // 1
```

## 블록 스코프 (block scope)
- 중괄호({}) 내부 가르킴
- 블록 스코프를 가지는 변수는 블록 바깥에서 접근 불가능
```js
let x = 1

if (x===1) {
  let x =2
  console.log(x) // 2
}
console.log(x) // 1
```
```js
let x = 1

if (x===1) {
  x =2
  console.log(x) // 2
}
console.log(x) // 2
```
## 함수 스코프
- 함수 중괄호 내부를 가리킴
- 함수 바깥에서 접근 불가능
```js
let x = 2
function foo() {
  let x = 1
  console.log(x) // 1
}
foo()
console.log(x) // 2
```
## 호이스팅 (hoisting)
- 변수를 선언 이전에 참조할 수 있는 현상
- var로 선언된 변수는 선언 이전에 참조할 수 있으며 이러한 현상 호이스팅이라고 함
- 변수 이전 이전에 위치에서 접근 시 undefined를 반환
- 


## 정리
- Airbnb 스타일 가이드에서는 기본적으로 const 사용 권장

![image](https://user-images.githubusercontent.com/122726684/232645564-3e3e4609-7829-4d62-9874-1c8989d4cdbb.png)


# 데이터 타입
## 분류
- JavaScript의 모든 값은 특정한 데이터 타입을 가짐
- 크게 원시 타입(primitive type)과 참조 타입(reference type)으로 분류됨

![image](https://user-images.githubusercontent.com/122726684/232645929-e6f0df50-a44f-4580-a056-5dd3e152ae44.png)

## 원시타입
### 1. Number
- 정수 또는 실수형 숫자를 표현하는 자료형
- NaN을 반환하는 경우
  - 숫자로서 읽을 수 없음
  - 결과가 허수
  - 피연한자가 NaN
  - 정의할 수 없는 계산식
  - 문자열을 포함하면서 덧셈이 아닌 계산식

![image](https://user-images.githubusercontent.com/122726684/232646203-91e95255-c056-45e7-896b-38b3790e708a.png)

### 2. String
- 문자열을 표현하는 자료형
- 작은 따옴표 또는 큰 따옴표 모두 가능
- 곱셈, 나눗셈, 뺄셈은 불가능, 덧셈으로 문자열끼리 붙일 수 있음
- escape sequence 사용 가능 
  - 줄 바꿈 시 '\n'사용
- TemplateLiteral을 사용하면 줄 바꿈 가능, 문자열 사이에 변수도 삽입 가능
  - TemplateLiteral: 내장된 표현식을 허용하는 문자열 작성 방식
  - backtick(` `) 이용며 $와 중괄호 사용하여 표현식 넣을 수 있음

![image](https://user-images.githubusercontent.com/122726684/232646343-9544df43-10bb-4ed7-be9d-ee5084ac120b.png)
![image](https://user-images.githubusercontent.com/122726684/232646364-06798d03-125a-4a48-9f2a-50173f86167d.png)
![image](https://user-images.githubusercontent.com/122726684/232646557-32f35098-4b32-4ab4-8f5c-bd196b4f5564.png)

### 3. NULL
- null 값을 나타내는 특별한 키워드
- 변수의 값이 없음을 의도적으로 표현할 때 사용
- typeof 을 통해 확인하면 null이 원시 타입임에도 object로 출력됨

![image](https://user-images.githubusercontent.com/122726684/232646875-bcac6f22-b907-4980-bd04-c0f861e5aed3.png)

### 3. Undefined
- 값이 정의되어 있지 않음을 표현하는 값
- 변수 선언 이후 직접 값을 할당하지 않으면 자동으로 할당됨
  
![image](https://user-images.githubusercontent.com/122726684/232647036-c479e1bd-548d-4e60-badc-32b051b86fd7.png)

### 4. Boolean
- true, false
- 조건문, 반복문에서 유용하게 사용
- 조건문, 반복문에서 boolean이 아닌 데이터 타입은 자동 형변환 규칙에 따라 true, false로 변환

## 참조 타입
### 1. 객체 Object
- 객체는 속성의 집합, 중괄호 내부에 key와 value의 쌍으로 표현
- key
  - 문자열 타입만 가능
  - key 이름에 띄어쓰기 등 구분자가 있으면 따옴표로 묶어서 표현
- value
  - 모든 타입(함수 포함) 가능
- 객체 요소 접근
  - 점(.) 또는 대괄호([])로 가능
  - key 이름에 띄어쓰기 같은 구분자가 있으면 대괄호 접근만 가능
  
![image](https://user-images.githubusercontent.com/122726684/232652506-5c216481-5521-44f1-b7bc-7a39e028a914.png)

### 2. 배열 Array
- 키와 속성들은 담고 있는 참조 타입의 객체
- 순서를 보장하는 특징
- 주로 대괄호를 이용하여 생성, 0 포함한 양의 정수 인덱스로 특정 값에 접근 가능
- 배열의 길이는 array.length 로 접근 가능

![image](https://user-images.githubusercontent.com/122726684/232652733-6c10e07d-f321-4277-8eda-ca9e07451cd9.png)

### 3. 함수 Function
- 함수 정의 방법은 2가지: 함수 선언식 / 함수 표현식
- 함수 선언식 (Function declaration)
```js
function 함수명(매개변수) {
  // ~
}
```
![image](https://user-images.githubusercontent.com/122726684/232653473-fb20b4a4-a81a-4f92-96d2-ba636020b8b2.png)

- 함수 표현식 (Function expression)
  - 함수의 이름을 생략한 익명 함수로 정의 가능
```js
keyword function_name = function(매개변수) {
  // do something
}
```
![image](https://user-images.githubusercontent.com/122726684/232653971-334d84a8-6679-45a6-9aa2-0ba367c6ff3b.png)

![image](https://user-images.githubusercontent.com/122726684/232654199-834b4810-151f-4b1b-907d-7b2113577717.png)

## 자동 형변환 (ToBoolean Conversions)

![image](https://user-images.githubusercontent.com/122726684/232654254-e98745d9-645e-4bd0-9d99-a49b42a026a1.png)

# 연산자
## 할당 연산자
![image](https://user-images.githubusercontent.com/122726684/232654980-2a9f537e-3536-4285-8591-30e19089c58c.png)
## 비교 연산자
- 피연산자들을 비교학 결과값을 boolean으로 반환하는 연산자
- 문자열은 유니코드 값을 사용하며 표준 사전 순서를 기반으로 비교
  - 알파벳 순서상 후순휘가 더 크다
  - 소문자가 대문자보다 더 크다

![image](https://user-images.githubusercontent.com/122726684/232655217-a2531a6e-6a6b-4563-83d3-b8296eb788cd.png)

## 동등 연산자(==)
- 비교할 때 암묵적 타입 변환 통해 타입 일치시킨 후 같은 값인지 비교
- 특별한 경우 제외하고 사용하지 않음
![image](https://user-images.githubusercontent.com/122726684/232655270-34484ec5-d0ca-4411-856a-058bccb63cea.png)

## 일치 연산자 (===)
- 두 피연자의 값과 타입이 모두 같은 경우 true 반환
- 같은 객체 가리키거나 같은 타입이면서 같은 값인지 비교
- 암묵적 타입 변환 발생하지 않음

![image](https://user-images.githubusercontent.com/122726684/232655707-fc21a5c6-910e-4580-9e95-179f8c90d7cf.png)

## 논리 연산자
- and &&
- or ||
- not !

![image](https://user-images.githubusercontent.com/122726684/232656928-fe6af698-283b-40b3-829d-e13ec9afd16a.png)

## 삼항 연산자
- 가장 앞의 조건식이 참이면 : 앞의 값 반환, 반대 일 경우 : 뒤의 값 반환

![image](https://user-images.githubusercontent.com/122726684/232657031-598a85bb-3d55-4cc6-8a27-932c42811880.png)

## 스프레드 연산자 
- 배열이나 객체를 전개하여 각 요소를 개별적인 값으로 분리하는 연산자

![image](https://user-images.githubusercontent.com/122726684/232657214-39c4664b-5474-4806-bf99-1bb81b998be6.png)

# 조건문, 반복문
## 조건문
### IF statement
- 조건은 소괄호 안에 작성
- 실행할 코드는 중괄호 안에 작성
- 블록 스코프 생성

![image](https://user-images.githubusercontent.com/122726684/232657433-6a3e5743-a00c-460a-9f91-04301d54025f.png)

## 반복문
### while
```js
while (조건문) {
   // do something
}
```

![image](https://user-images.githubusercontent.com/122726684/232658501-396f2351-ba18-4714-ad5e-e94e1c7c1214.png)

### for
```js
for ([초기문];[조건문];[증감문]) {
  // do something
}
```

![image](https://user-images.githubusercontent.com/122726684/232658553-a7b4bf54-30d2-458c-967c-d3a7215dbafc.png)

### for in
```js
for (variable in objects) {
  statements
}
```
- 객체의 속성을 순회할 때 사용
- 배열도 순회 가능하지만 인덱스 순으로 순회한다는 보장이 없으므로 권장하지 않음
- 예시
```js
const fruits = {a:'apple', b:'banana'}
for (const key in fruits) {
  console.log(key) // a, b
  console.log(fruits[key]) // apple, banana
}
```
### for of
```js
for (variable of object) {
  statements
}
```
- 반복한 가능한 객체를 순회할 때 사용
- 반복한 가능한 객체의 종류: Array, Set, String 등
- 예시
```js
const = numbers = [0,1,2,3]
for (const num of numbers) {
  console.log(num) // 0,1,2,3
}
```
- array에서 for...in 은 index 반환
```js
const arr =[3,5,7]
for (const i in arr){
  console.log(i) // 0 1 2
}
```
## for문 /for..in 와 for..of
- for문
  - `for (let i==0;i<arr.length;i++)`의 경우에는 최초 정의한 i를 재할당 하면서 사용하기 때문에 const를 사용하면 에러
- for .. in, for...of
  - 재할당이 아니라 매 반복 시 해당 변수를 새로 정의하여 사용하므로 에러가 발생하지 않음
  
## Array.forEach()
- 배열의 메서드 중 하나
```js
Array.forEach(function(params)) {
  //code
}
```
- 예시
```js
const numbers = [1,2,3]
Array.forEach(function(element)) {
  console.log(element)
}
```
## 정리
![image](https://user-images.githubusercontent.com/122726684/232661227-c685e956-c1d3-480b-be83-9ede5e7e7d60.png)

## optional chaining
- `?.` : 뒤에 내용 우선 무시
- `??` : 앞의 내용 undefined/null 이면 뒤에꺼
```js
const obj = {
  a:1
}
console.log(obj.a) // 1
console.log(obj.a.value) // undefined
// console.log(obj.b.value) ERROR
console.log(obj.b?.value) // undefined
console.log(obj.b?.value ?? 'hoho')  // hoho
```

