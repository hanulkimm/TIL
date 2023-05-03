# CLI
## Vue CLI 프로젝트 구조
![image](https://user-images.githubusercontent.com/122726684/235554104-15c3abff-7bd7-4035-903e-6b55164de7c2.png)
### node-modules
- node.js 환경의 여러 의존성 모듈
- .gitignore 넣어줘야 함
### Babel
- JS의 ES6+ 코드를 구버전으로 번역/변환 해주는 도구
- JS의 파편화, 표준화의 영향으로 작성된 코드의 스펙트럼이 매우 다양
  - 최신 문법을 사용해도 브라우저의 버전 별로 동작하지 않는 상황이 발생
  - 버전에 따른 같은 의미의 다른 코드를 작성하는 등의 대응이 필요해졌고 이러한 문제를 해결하기 위한 도구
  - 원시 코드(최신 버전)를 목적 코드(구 버전)으로 옮기는 번역기가 등장하면서 더 이상 코드가 특정 브라우저에서 동작하지 않는 상황에 대해 크게 고민하지 않을 수 있음
### Module
- 분리된 파일 각각이 모듈 (js 파일 하나 하나가 모듈)
- 기능 단위로 분리
- 의존성 문제 : 모듈의 수가 많아지고 라이브러리 혹은 모듈 간의 의존성이 깊어지면서 특정한 곳에서 발생한 문제가 어떤 모듈 간의 문제인지 파악하기 어려움
  - Webpack이 의존성 문제를 해결하기 위해 등장
### Bundler
- 모듈 의존성 문제를 해결해주는 작업이 Bundling
- 이러한 일을 해주는 도구가 Bundler, Webpack은 다양한 bundler 중 하나
- 모듈들을 하나로 묶어주고 묶은 파일은 하나로 만들어짐
- bundling된 결과물은 개별 모듈의 실행 순서에 영향 받지 않고 동작하게 됨
### package-json
- 프로젝트의 종속성 목록과 지원되는 브라우저에 대한 구성 옵션을 포함
### package-lock.json
- node_modules에 설치되는 모듈과 관련된 모든 의존성을 설정 및 관리
- 협업 및 배포 환경에서 정확히 동일한 종속성을 설치하도록 보장하는 표현
- 사용할 패키지의 버전 고정
- 개발 과정 간의 의존성 패키지 충돌 방지

### public/index.html
- vue 앱의 뼈대가 되는 html 파일
- vue 앱과 연결된 요소가 있음

### src
- src/assets : 정적 파일을 저장하는 디렉토리
- src/components : 하위 컴포넌트들이 위치
- src/App.vue : 최상위 컴포넌트, public/index.html과 연결됨
- src/main.js : webpack이 필드를 시작할 때 가장 먼저 불러오는 entry point
  - public/index.html과 src/App.vue를 연결시키는 작업이 이루어지는 곳
  - Vue 전역에서 활용할 모듈을 등록할 수 있는 파일

# Component
## 개념
- UI를 독립적이고 재사용 가능한 조각들로 나눈 것
  - 기능별로 분화한 코드 조각
- CS에서는 다시 사용할 수 있는 범용성을 위해 개발된 소프트웨어 구성 요소 의미
- 유지보수가 쉬워지고 재사용성의 측면에서도 매우 강력한 기능

# SFC (Single File Component)
- 하나의 .vue 파일이 하나의 vue instance이고 하나의 컴포넌트임
- vue instance에서는 html, css, javascript 코드를 한 번에 관리

## Vue component 구조
### 템플릿 (HTML)
- html의 body 부분
- 눈으로 보여지는 요소 작성
- 다른 컴포넌트를 html 요소 처럼 추가 가능
### 스크립트 (JavaScript)
- JavaScript 코드가 작성되는 곳
- 컴포넌트 정보, 데이터, 메서드 등 vue instance를 구성하는 대부분이 작성 됨
### 스타일(CSS)
- CSS가 작성되며 컴포넌트의 스타일 담당
  
## 정리 
- 컴포넌트들이 tree 구조를 이루어 하나의 페이지를 만듦
- root에 해당하는 최상단의 component가 App.vue
- 이 App.vue를 index.html과 연결
- index.html 파일 하나만을 rendering

# Vue Component 실습
## 새로운 component 만들기
1. src 폴더 안의 component 폴더 안에 myComponent.vue 생성
2. script에 이름 등록
3. template에 요소 추가
- templates 안에는 반드시 하나의 요소만 추가 가능
- 비어 있으면 안됨
- 해당 요소 안에 추가 요소 작성해야 함

![image](https://user-images.githubusercontent.com/122726684/235588387-f2def18c-37f7-461b-9728-7eeb63d01451.png)

## component 등록 3단계
1. 불러오기
- `import {instance name} from {위치}`
- @는 src의 shortcut
- .vue는 생략 가능
2. 등록하기
3. 보여주기

![image](https://user-images.githubusercontent.com/122726684/235588668-e784d56c-9fb7-448a-999b-f0678c79984d.png)

## 자식 컴포넌트 작성
- src/components/ 안에 MyChild.vue 생성

![image](https://user-images.githubusercontent.com/122726684/235588850-cc7bec2f-e330-45a0-ab2d-ddfa20b6fd36.png)

- MyComponent에 MyChild 등록

![image](https://user-images.githubusercontent.com/122726684/235588904-f677518c-e5de-47ac-b66e-51847b98856e.png)

# Vue Data Management
## 개요
- 한 페이지 내에서 같은 데이터 공유해야 함
  - 페이지들은 component으로 구분되어 있음
- MyComponent에 정의된 data를 MyChild에서 사용하려면 어떻게?
- component는 부모-자식 관계를 가지므로 부모-자식 관계만 데이터를 주고받게 함
  - 데이터 흐름 파악 용이
  - 유지 보수하기 쉬워짐

![image](https://user-images.githubusercontent.com/122726684/235810633-241a15fc-60dc-4de6-9f49-247e3629782a.png)

- 부모 -> 자식 으로의 데이터 흐름: pass props 방식
- 자식 -> 부모로의 데이터 흐름: emit event 방식

## Pass Props
- 요소의 속성(property)을 사용하여 데이터 전달
- props는 부모(상위) 컴포넌트의 정보를 전달하기 위한 사용자 지정 특성
- 자식(하위) component는 props 옵션을 사용하여 수신하는 props를 명시적으로 선언해야 함
- 예시: App.vue의 `<HelloWorld/>` 요소에 `msg="~"`라는 property를 설정하였고, 하위 컴포넌트인 HelloWorld는 자신에게 부여된 msg property를 template에서 {{msg}}의 형태로 사용한 것

![image](https://user-images.githubusercontent.com/122726684/235811945-07f987f8-462e-4f94-bfd1-b0bbe12134c8.png)

### staticProps
- 정적인 데이터를 전달하는 경우 static props라고 명시하기도 함
- 요소에 속성을 작성하듯이 사용 가능하며, `prop-data-name="value"`의 형태로 데이터를 전달하여 이때 속성의 키 값은 kebab-case를 사용

![image](https://user-images.githubusercontent.com/122726684/235812709-230ca07d-77c9-498c-9e7a-f7a2e1f10442.png)  
![image](https://user-images.githubusercontent.com/122726684/235812726-150a6afc-7c2f-4601-9162-b73c06b24636.png)

### Pass Props convention
- 부모에서 넘겨주는 props: kebab-case (HTML 속성명은 대소문자를 구분하기 않기 때문)
- 자식에서 받는 props: camel-case
- 부모 템플릿(html)에서 kebab-case로 넘긴 변수를 자식의 스크립트(vue)에서 자동으로 camelCase로 변환하여 인식함

### Dynamic Props
- 변수를 props로 전달할 수 있음
  - 각 vue 인스턴스는 같은 data 객체를 공유하므로 새로운 data 객체를 반환하여 사용해야 함  
  ![image](https://user-images.githubusercontent.com/122726684/235813572-f8bca0d5-aa84-414e-9fd2-baca73d71e56.png)

- v-bind directive를 사용해 데이터를 동적으로 바인딩
- 부모 컴포넌트의 데이터가 업데이트 되면 자식 컴포넌트로 전달되는 데이터 또한 업데이트 됨

![image](https://user-images.githubusercontent.com/122726684/235813480-4170fe2c-2ea2-4956-b401-08c2fc4ace93.png)

- `:dynamic-props="dynamicProps"`는 앞의 key 값(dynamic-props)이란 이름으로 뒤의 " "안에 오는 데이터(dynamicProps)를 전달하겠다는 뜻
- 즉 `:my-props:"dynamicProps"`로 데이터를 넘긴다면 자식 컴포넌트에서 myProps로 데이터를 받아야 함

![image](https://user-images.githubusercontent.com/122726684/235814194-4e33fa9b-921f-4a6d-830b-9174fad55b5c.png)

- v-bind로 묶여있는 " "안의 구문은 javascript의 구문으로 볼 수 있음
  - dynamicProps라고 하는 변수에 대한 data를 전달할 수 있는 것

### 단방향 데이터 흐름
- 모든 props는 부모에서 자식으로 즉 아래로 단방향 바인딩 형성
- 부모 속성이 업데이트 되면 자식으로 흐르지만 반대 방향은 아님
  - 부모 컴포넌트가 업데이트 될 떄마다 자식 컴포넌트의 모든 prop들이 최신 값으로 새로고침 됨
- 목적: 하위 컴포넌트가 실수로 상위 컴포넌트 상태로 변경하여 앱의 데이터 흐름을 이해하기 힘들게 만드는 것을 방지
- 하위 컴포넌트에서 prop를 변경하려고 시도해서는 안되며 그렇게 하면 Vue는 콘솔에서 경고를 출력함

## Emit Event
- 부모 컴포넌트에서 자식 컴포넌트로 데이터를 전달 할때는 이벤트를 발생 시킴
- 어떻게 데이터 전달?
  - 데이터를 이벤트 리스너의 콜백함수의 인자로 전달
  - 상위 컴포넌트는 해당 이벤트를 통해 데이터 받음
### `$emit`
- `$emit` 메서드를 통해 부모 컴포넌트에 이벤트 발생
- `$emit(event-name)`형식으로 사용하며 부모 컴포넌트에 event-name이라는 이벤트가 발생했다는 것을 알림
### Emit Event 예시
1. 자식 컴포넌트에 버튼 만들고 클릭 이벤트 추가
2. $emit 통해 부모 컴포넌트에 child-to-parent 이벤트 트리거
3. emit된 이벤트를 상위 컴포넌트에서 청취 후 핸들러 함수 실행

![image](https://user-images.githubusercontent.com/122726684/235818284-b16d363b-e483-4ce8-a91a-6b79045dc75b.png)

![image](https://user-images.githubusercontent.com/122726684/235818295-35e4985e-0447-4917-bd73-ead7324991cf.png)

## Emit with Data
- 이벤트 발생(emit)시킬 때 인자로 데이터 전달 가능
- 전달된 데이터는 이벤트와 연결된 부모 컴포넌트의 핸들러 함수의 인자로 사용 가능

![image](https://user-images.githubusercontent.com/122726684/235818463-924b65da-c5d2-4b73-a170-3ec8a1df349f.png)

![image](https://user-images.githubusercontent.com/122726684/235818693-9f3ae126-8899-4568-bace-74c1ef624219.png)

## Emit with DynamicData
![image](https://user-images.githubusercontent.com/122726684/235818855-1139bbd0-a5d2-41e5-91c1-754e943e9e7f.png)  
![image](https://user-images.githubusercontent.com/122726684/235818873-a12e6328-5104-402a-a624-8d8b4e722d83.png)

## pass props/emit event 컨벤션
- html요소에서 사용할 떄는 kebab-case
- JavaScript에서 사용할 떄는 camelCase
### props
- 상위-> 하위 흐름에서 html 요소로 내려줌: kebab-case
- 하위에서 받을 때는 JavaScript에서 받음: camelCase
### emit
- emit 이벤트를 발생시키면 HTMl 요소가 이벤트를 청취함: kebab-case
- 메서드, 변수명 등은 JavaScript에서 사용함: camelCase

# Lifecycle Hooks
