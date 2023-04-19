# 함수
## 매개변수와 인자의 개수 불일치 허용
- 매개변수보다 인자의 개수가 많을 경우
```js
const noArgs = function () {
  return 0
}
noArgs(1,2,3) // 0

const twoArgs = function (arg1, arg2) {
  return [arg1, arg2]
}
twoArgs(1,2,3) // [1,2]
```
- 매개변수보다 인자의 개수가 적을 경우
```js
const threeArgs = function (arg1, arg2, arg3) {
  return [arg1, arg2, arg3]
}

console.log(threeArgs()) // [ undefined, undefined, undefined ]
console.log(threeArgs(1)) // [ 1, undefined, undefined ]
console.log(threeArgs(2,3)) // [ 2, 3, undefined ]
```
## Spread Syntax
- '전개 구문'
- 전개 구문을 사용하면 배열이나 문자열과 같이 반복 가능한 객체를 배열의 경우는 요소, 함수의 경우는 인자로 확장할 수 있음
### 1. 배열과의 사용
```js
let parts = ['어깨', '무릎']
let lyrics = ['머리', ...parts, '발']
console.log(lyrics)
```
### 2. 함수와의 사용
```js
const restOpr = function (arg1, arg2, ...restArgs) {
  return [arg1, arg2, restArgs]
}

console.log(restOpr(1,2,3,4,5)) // [ 1, 2, [ 3, 4, 5 ] ]
console.log(restOpr(1,2)) // [ 1, 2, [] ]
```
## 호이스팅 - 선언식
- 함수 선언식으로 정의한 함수는 var로 정의한 변수처럼 호이스팅이 발생
- 즉, 함수 호출 이후에 선언해도 동작함
```js
sum(2,7)
function sum(n1, n2) {
  return n1+n2
}
```
## 호이스팅 - 표현식
- 표현식으로 선언한 함수는 함수 정의 전에 호출 시 에러 발생
- 함수 표현식으로 정의된 함수는 변수로 평가되어 변수의 scope 규칙을 따름

# Arrow Function
## 개념
- 함수를 비교적 간결하게 정의할 수 있는 문법
- function 키워드 생략 가능
- 매개변수가 하나 뿐이라면 매개변수의 '()' 생략 가능
- 함수의 내용이 한 줄이라면 '{}'와 return도 생략 가능
- 항상 익명 함수
  - 함수 표현식에서만 사용!
- 명확성과 일관성을 위해 항상 인자 주위에는 괄호를 포함하는 것을 권장
```js
const arrow = function (name) {
  return `hello, ${name}`
}

// 1. function 키워드 생략
const arrow1 = (name) => {return `hello, ${name}`}
// 2. 인자 1개인 경우 () 생략 가능
const arrow2 = name => {return `hello, ${name}`}
// 3. return 표현식 1개일 경우 {} & return 삭제 가능
const arrow3 = name => `hello, ${name}`

console.log(arrow3('하늘')) // hello, 하늘
```
```js
// 1. 인자가 없다면
let noArgs = () => 'No args'

// 2-1 object return
let returnObject = () => { return {key: 'value'}}
// 2-2 return 적지 않으려면 괄호 붙이기
let returnObject = () => ({key:'value'})
```

# this
## 개념
- 어떠한 object를 가리키는 키워드
- JS의 함수는 호출된 때 this를 암묵적으로 전달 받음
- 함수 호출 방식에 따라 this에 바인딩 되는 객체가 달라짐
- 함수가 어떻게 호출 되었는지에 따라 동적으로 결정됨
## 1. 전역 문맥에서의 this
- 브라우저의 전역 객체인 window 가리킴
  - 전역 객체: 모든 객체의 유일한 최상위 객체
```js
const myFunc = function() {
  console.log(this)
}

myFunc() // global (브라우저에서는 window)
```
## 2. 함수 문맥에서의 this
- this의 값은 함수를 호출한 방법에 의해 결정됨
### 1. 단순 호출
- 전역 객체를 가리킴
- 브라우저에서 전역은 window를 의미함
```js
const muFunc = function () {
  console.log(this)
}
// 브라우저
myFunc() // window
```
### 2. Method (Function in Object)
- 메서드를 선언하고 호출한다면 객체의 메서드이므로 해당 객체가 바인딩
```js
const myObj = {
  data:1,
  myFunc() {
    console.log(this) // { data : 1, myFunc: [Function: myFunc] }
    console.log(this.data) // 1
  }
}
myObj.myFunc()
```
### 3. Nested (Function 키워드)
- forEach 의 콜백 함수에서의 this가 메서드의 객체를 가리키지 못하고 전역 객체 window를 가리킴
- 단순 호출 방식으로 사용되었기 때문
- 이를 해결하기 위해 'Arrow function' 사용
```js
const myObj = {
  numbers:[1],
  myFunc() {
    console.log(this) //{ numbers: [1], myFunc: [Function: myFunc] }
    this.numbers.forEach(function (num){
      console.log(num) // 1
      console.log(this) // global
    })
  }
}
myObj.myFunc()
```
### Nested (화살표 함수)
- 메서드의 객체를 가리킴
- 화살표 함수에서 this는 자신을 감싼 정적 범위
- 자동으로 한 단계 상위의 scope의 context를 바인딩
```js
const myObj = {
  numbers:[1],
  myFunc() {
    console.log(this) //{ numbers: [1], myFunc: [Function: myFunc] }
    this.numbers.forEach((num) =>{
      console.log(num) // 1
      console.log(this) // { numbers: [1], myFunc: [Function: myFunc] }
    })
  }
}
myObj.myFunc()
```
### 화살표 함수
- 호출의 위치과 상관없이 상위 스코프를 가리킴
- Lexical scope: 함수를 어디서 호출하는지가 아니라 어디에 선언하였는지에 따라 결정
- 함수 내의 함수 상황에서는 화살표 함수를 쓰는 것을 권장
```js
let x = 1 

function first() {
  let x =10
  second()
}

function second() {
  console.log(x)
}

first() // 1
second() // 1
```
# Array 배열
## 개념
- 키와 속성들을 담고 있는 참조 타입의 객체
- 순서를 보장하는 특징
- 주로 대괄호 이용하여 생성하고 0을 포함한 인덱스로 특정 값에 접근 가능
- 배열의 길이는 array.length 형태로 접근 가능

![image](https://user-images.githubusercontent.com/122726684/232952232-55382f72-5de4-4261-b42d-2ac266416a25.png)


## 배열 메서드 기초
![image](https://user-images.githubusercontent.com/122726684/232952274-c6f987d6-1d72-4d8c-a887-bddcb1ae6797.png)

### `array.reverse()`
```js
const numbers = [1,2,3,4,5]
numbers.reverse()
console.log(numbers) //[ 5, 4, 3, 2, 1 ]
```
### `array.push`, `array.pop`
```js
const numbers = [1,2,3,4,5]
numbers.push(100)
console.log(numbers) //[ 1, 2, 3, 4, 5, 100 ]
numbers.pop()
console.log(numbers) // [ 1, 2, 3, 4, 5 ]
```
### `array.includes(value)`
- 배열에 특정 값이 존재하는지 판별 후 true 또는 false 반환

![image](https://user-images.githubusercontent.com/122726684/232953009-76b67cb7-c98b-48d5-a634-1a6b0207bb57.png)

### `array.indexOf(value)`
- 배열에 측정 값이 존해하는지 확인 후 가장 첫번째 요소의 인덱스 반환
- 만약 해당 값이 없을 경우 -1 반환

![image](https://user-images.githubusercontent.com/122726684/232953208-f6a86d98-eba2-43f7-8cc4-fde2a0f971a0.png)

## 배열 메서드 심화
### Array Helper Methods
  - 배열 순회하면 특정 로직 수행하는 메서드
  - 메서드 호출 시 인자로 callback 함수를 받는 것이 특징
    - 콜백 함수 : 다름 함수의 인자로 전달되는 함수
  
![image](https://user-images.githubusercontent.com/122726684/232953341-2f8b877f-1949-4edd-9866-b8d47ad0f8d1.png)

## forEach
![image](https://user-images.githubusercontent.com/122726684/232955119-de61e622-7780-49c5-8dcf-63f92b8480b6.png)

- 인자로 주어지는 함수를 배열의 각 요소에 대해 한 번씩 실행
- 콜백 함수는 3개의 매개변수로 구성
  - 1. element: 배열 요소
  - 2. index 
  - 3. array : 배열 자체
- 반환 값 return 없음
```js
const colors = ['red', 'blue', 'green']
// 1. 
printFunc = function (color) {
  console.log(color)
}
colors.forEach(printFunc)
//red
// blue
// green

// 2. 함수 정의를 인자로 넣어보기
colors.forEach(function (color, index, array) {
  console.log(color)
  console.log(index)
  console.log(array)
})
// 0
// [ 'red', 'blue', 'green' ]
// blue
// 1
// [ 'red', 'blue', 'green' ]
// green
// 2
// [ 'red', 'blue', 'green' ]

// 3. 화살표 함수 적용
colors.forEach((color)=>{
  return console.log(color)
})
```

### map
![image](https://user-images.githubusercontent.com/122726684/232955482-cd6f583e-cc9b-4069-afd0-4c303a5b5383.png)

- 배열의 각 요소에 콜백 함수를 한 번씩 실행
- 콜백 함수의 반환 값을 요소로 하는 새로운 배열 반환
- 기존 배열 전체를 다른 형태로 바꿀 때 유용
  - forEach + return 느낌

![image](https://user-images.githubusercontent.com/122726684/232955732-61d15c37-829f-423d-891c-78d9de5c0b76.png)

### filter
![image](https://user-images.githubusercontent.com/122726684/232955788-b70c76ca-98f0-4def-b9ac-099f0da1e9c6.png)

- 콜백 함수의 반환 값이 true인 요소들만 모아서 새로운 배열 반환

![image](https://user-images.githubusercontent.com/122726684/232955906-77617910-cad3-4395-b938-3ed99339b342.png)

### reduce
![image](https://user-images.githubusercontent.com/122726684/232955969-5d534f7f-f989-4079-9c48-f70e2c5abb8c.png)

- 배열을 하나의 값으로 계산하는 동작이 필요한 경우 사용( 총합, 평균 등)
- map, filter 등 여러 배열 메서드 동작을 대부분 대체할 수 있음
- 주요 매개변수
  - acc : 반환 값이 누적되는 변수
  - initial value : 최초 callback 함수 호출 시 acc에 할당하는 값

![image](https://user-images.githubusercontent.com/122726684/232956313-407441d6-c660-455d-9418-e1608aa3d1e1.png)

### find
![image](https://user-images.githubusercontent.com/122726684/232956364-5d8e9b24-5c85-4430-b483-5995421e196f.png)

- 콜백 함수의 반환 값이 true면, 조건 만족하는 첫번째 요소 반환
- 찾는 값이 배열에 없으며 undefined 반환

![image](https://user-images.githubusercontent.com/122726684/232956490-1611cc56-e268-4afa-8429-2e24c36a656e.png)

### some
- 모든 요소가 통과하지 못하면 거짓 반환
- 빈 배열은 항상 false 반환
  
![image](https://user-images.githubusercontent.com/122726684/232956677-e02eedbd-f9b3-4357-a2ce-4693926f59c7.png)

### every
![image](https://user-images.githubusercontent.com/122726684/232956694-f1d565b4-c7a5-4a12-b8a7-5c76ab68b75c.png)

- 하나의 요소라도 통과하지 못하면 false 반환
- 빈 배열은 항상 true

![image](https://user-images.githubusercontent.com/122726684/232956759-064bd89d-08ea-47d5-b880-c3ab248d2f24.png)

## 배열 순회 비교
![image](https://user-images.githubusercontent.com/122726684/232956802-e5dfd4ed-57de-423c-acec-0076f40d123e.png)

# 객체
## 개념
- 속성의 집합, 중괄호 내부에 key와 value의 쌍으로 표현
- key: 문자열 타입만 가능
- value: 모든 타입(함수 포함) 가능
- 객체 요소 접근: 점이나 대괄호
- 함수 정의 예시

![image](https://user-images.githubusercontent.com/122726684/232956993-896873d9-2d85-4ef0-995c-8d4e4eee5a9a.png)

## 객체 관련 문법
### 1. 속성명 축약
- 객체를 정의할 때 key와 할당하는 변수의 이름이 같으면 예시와 같이 축약 가능
```js
const books = ['JavaScript', 'Python']
const magazines = ['Vogue', 'Science']

const bookShop = {
  books,
  magazines,
}

console.log(bookShop)
// {
//   books: [ 'JavaScript', 'Python' ],
//   magazines: [ 'Vogue', 'Science' ]
// }
```
### 2. 메서드명 축약
- 메서드 선언 시 function 키워드 생략 가능
```js
// ES5
const obj = {
  greeting : function() {
    console.log('hi')
  }
}
obj.greeting()

// ES6+
const obj = {
  greeting() {
    console.log('hi')
  }
}
obj.greeting()
```
### 3. 계산된 속성 (computed property name)
- 객체를 정의할 때 key의 이름을 표현식을 이용하여 동적으로 생성 가능
```js
const key = 'country'
const value = ['한국', '미국', '일본', '중국']
const myObj = {
  [key]: value
}

console.log(myObj) // { country: [ '한국', '미국', '일본', '중국' ] }
console.log(myObj.country) // [ '한국', '미국', '일본', '중국' ]
```
### 4. 구조 분해 할당 (destructing assignment)
- 배열 또는 객체를 분해하여 속성을 변수에 쉽게 할당 할 수 있는 문법
```js
const userInformation = {
  name : 'Hanul Kim',
  userID : 'ssafy',
  email : 'ssafy@naver.com'
}
const {name} = userInformation
console.log(name)
```

### 5. Spread Syntax(...)
```js
const obj = {b:2, c:3, d:4}
const newObj = {a:1, ...obj, e:5}
console.log(newObj) // { a: 1, b: 2, c: 3, d: 4, e: 5 }
```