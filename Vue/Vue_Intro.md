# Vue

## Front-end Development
### 개요
- Web App 또는 Web site의 UI/UX를  제작하고 관리하는 과정
- Front-end 프레임워크와 라이브러리(vue.js)를 사용하여 개발 효율성을 높이고 Web App의 복잡성을 관리
- Front-end 개발에 사용되는 주요 기술은 HTML,CSS,JavaScript

### Web app
- 웹 브라우저에서 실행되는 애플리케이션 소프트웨어
- 개발자 도구 > 디바이스 모드
- 웹 페이지가 그대로 보이는 것이 아닌 디바이스에 설치된 App처럼 보이는 것
- 웹 페이지가 디바이스에 맞는 적절한 UI/UX로 표현되는 형태

### SPA(Single Page Application)
- 이전까지는 사용자의 요청에 따라 적절한 페이지 별 template 반환
- SPA는 서버에서 최초 1장의 HTML만 전달받아 모든 요청에 대응하는 방식
  - CSR(Client Side Rendering) 방식으로 요청을 처리하기 때문

### 참고 SSR(Server Side Rendering)
- 기존의 요청 처리 방식은 SSR
- Server가 사용자의 요청에 적합한 HTMl을 렌더링하여 제공하는 방식
- 전달 받은 새 문서를 보여주기 위해 브라우저는 새로고침을 진행

## CSR (Client Side Rendering)
- 최초 한 장의 HTML을 받아오는 것은 동일
- server로 부터 최초로 받아오는 문서는 빈 html anstj
- 각 요청에 대한 대응을 JS를 사용하여 필요한 부분만 다시 렌더링
1. 필요한 페이지를 서버에 AJAX로 요청
2. 서버는 화면에 그리기 위해 필요한 데이터를 JSON 방식으로 전달
3. JSON 데이터를 JS로 처리,DOM 트리에 반영(렌더링)

![image](https://user-images.githubusercontent.com/122726684/234729497-e0d01d18-4627-432a-bb76-6a09c537c014.png)

### 왜 CSR 방식 사용?
1. 모든 HTMl 페이지를 서버로부터 받아서 표시하지 않아도 됨
- 클라이언트-서버간 통신 -> 트래픽 감소 -> 응답 속도 빨라짐
2. 매번 새 문서를 받아 새로고침 하는 것이 아니라 필요한 부분만 고쳐 나가므르 각 요쳥이 끊임없이 진행
3. BE와 FE의 작업 영역을 명확히 분리 할 수 있음
- 각자 맡은 역할을 명확히 분리함 -> 협업이 용이해짐

### CSR 단점
- 첫 구동 시 필요한 데이터가 많으면 많을수록 최초 작동 시작까지 오랜 시간이 소요
- 검색 엔진 최적화(SEO, Search Engine Optimization)가 어려움
  - 대체적으로 HTML에 작성된 내용을 기반으로 하는 검색 엔진에 빈 HTML을 공유하는 SPA 서비스가 노출되기는 어려움

## Vue 사용해보기
1. Vue CDN 가져오기
2. Vue instance 생성
3. el, data 설정

![image](https://user-images.githubusercontent.com/122726684/234747548-46184358-41bc-438d-ae22-d0235933fb32.png)

### el (element)
- Vue instance와 DOM을 연결하는 옵션
- Vue instance와 연결되지 않은 DOM 외부는 Vue의 영향을 받지 않음
  - Vue 속성 및 메서드 사용 불가
- 예시:
  - 새로운 Vue instance 생성
  - 생성자 함수 첫번째 인자로 Object 작성

```html
<div id = 'app'>
</div>

<script>
  const app new Vue({
    el : '#app',
  })
</script>
```

### data
- Vue instance의 데이터 객체 혹은 인스턴스 속성
- 데이터 객체는 반드시 기본 객체 {} (object)여야 함
- 객체 내부 아이템들은 value로 모든 타입의 객체를 가질 수 있음
- 정의된 속성은 interpolation`{{}}`을 통해 view에 렌더링 가능
- 예시:
  - vue instance에 data 객체 수가
  - data 객체에 message 값 추가
  - 추가된 객체의 각 값들은 this.message 형태로 접근 가능

```html
<div id = 'app'>
  {{message}}
</div>

<script>
  const app new Vue({
    el : '#app',
    data : {
      message : 'Hello, Vue!'
    },
  })
</script>
```

### methods
- Vue instance의 method들을 정의하는 곳
- methods 객체 정의
  - 객체 내 print method 정의
  - print method 실행 시 Vue instance의 data 내 message 출력
- console 창에 app.print() 실행
```html
<div id = 'app'>
  {{message}}
</div>

<script>
  const app new Vue({
    el : '#app',
    data : {
      message : 'Hello, Vue!'
    },
    methods : {
      print : function() {
        console.log(this.message)
      }
    }
  })
</script>
```
- method를 호출하여 data 변경 가능
  - 객체 내 bye method 정의
  - print method 실행 시 Vue instance의 data내 message 변경
- 콘솔창에서 app.bye() 실행
```html
<div id = 'app'>
  {{message}}
</div>
<script>
  const app new Vue({
    el : '#app',
    data : {
      message : 'Hello, Vue!'
    },
    methods : {
      print : function() {
        console.log(this.message)
      },
      bye(){
        this.message = 'Bye, Vue!'
      }
    }
  })
</script>
```

### 주의 (Arrow Function)
- 메서드를 정의할 때, arrow function을 사용하면 안됨
- arrow function의 this는 함수가 선언될 때 상위 스코프를 가리킴
- this가 상위 객체 window를 가리킴
- 호출은 문제 없이 가능하나 this로 vue의 data를 변경하지 못함

