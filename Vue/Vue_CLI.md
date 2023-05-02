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