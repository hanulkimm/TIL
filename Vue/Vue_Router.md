# UI & UX
## UX (User Experience)
- 유저와 가장 가까이 있는 분야, 데이터를 기반으로 유저를 조사하고 분석해서 개발자, 디자이너가 이해할 수 있게 소통
- 유저가 느끼는 느낌, 태도 그리고 행동을 디자인

## UI (User Interface)
- 유저에게 보이는 화면을 디자인
- UX를 고려한 디자인을 반영, 이 과정에서 기능 개선 혹은 추가가 필요한 경우 front-end 개발자와 가장 많이 소통

## Interface
- 서로 다른 두 개의 시스템, 장치 사이에서 정보나 신호를 주고받는 경우의 접점
  - 사용자가 기기를 쉽게 동작시키는데 도움을 주는 시스템
- 예시: CLI(command-line interface)나 GUI(Graphic user Interface)

# Vue Router
## Routing
- 네트워크에서 경로를 선택하는 프로세스
- 웹 서비스에서의 라우팅
  - 유저가 방문한 URL에 대해 적절한 결과를 응답하는 것

## Routing in SSR
- Server가 모든 라우팅 통제
- URL로 요청이 들어오면 응답으로 완성된 HTML 제공
- Routing(URL)에 대한 결정권을 서버가 가짐

## Routing in SPA / CSR
- 서버는 하나의 HTMl(index.html)만을 제공
- 이후에 모든 동작은 HTML 문서 위에서 JavaScript 코드를 활용
  - DOM을 그리는데 필요한 추가적인 데이터가 있다면 axios와 같은 AJAX 요청을 보낼 수 있는 도구를 사용하여 데이터를 가져오고 처리
- 하나의 URL만 가질 수 있음

## Routing 필요성
- routing이 없다면
  - 유저가 URL을 통해 페이지의 변화를 감지할 수 없음
  - 무엇을 렌더링 중인지에 대한 상태를 알 수 없음
  - 브라우저의 뒤로 가기 기능을 사용할 수 없음

## Vue Router
![image](https://user-images.githubusercontent.com/122726684/236976221-a62a0bd7-6ec7-4bdc-b14d-f917075ec415.png)
![image](https://user-images.githubusercontent.com/122726684/236976237-84881636-3f63-499c-8bbf-04f8d47e74bd.png)
![image](https://user-images.githubusercontent.com/122726684/236976303-0fb2906a-c3eb-4ad2-b0f4-6edd77f9d87b.png)

### router-link
- url을 이동시킴
  - routes에 등록된 컴포넌트와 매핑됨
  - 히스토리 모드에서 router-link는 클릭 이벤트를 차단하여 a 태그와 달리 브라우저가 페이지를 다시 로드하지 않도록 함
- 목표 경로는 'to'속성으로 지정됨
- 기능에 맞게 HTML에서 a 태그로 rendering되지만, 필요에 따라 다른 태그로 바꿀 수 있음

### router-view
- 주어진 URL에 대해 일치하는 컴포넌트를 렌더링 하는 컴포넌트
- 실제 component가 DOM에 부착되어 보이는 자리를 의미
- router-link를 클릭하면 routes에 매핑된 컴포넌트를 렌더링

## src/router/index.js
- 라우터에 관련된 정보 및 설정이 작성 되는 곳
- Django에서의 url.py에 해당
- routes에 URL와 컴포넌트를 매핑

![image](https://user-images.githubusercontent.com/122726684/236978644-f2d1e554-5f51-4ea4-b73b-41a05a8cc482.png)

## src/Views
- router-view에 들어갈 component 작성
- 기존에 컴포넌트를 작성하던 곳은 component 폴더 뿐이었지만 이제 두 폴더로 나뉘어짐
- 각 폴더 안의 .vue파일들이 기능적으로 다른 것은 아님
### src/views/
- routes에 매핑되는 컴포넌트
- route-view의 위치에 렌더링되는 컴포넌트 모아두는 폴더
- 다른 컴포넌트와 구분되게 이름은 View로 끝나도록 만드는 것을 권장
### src/components/
- routes에 메핑된 컴포넌트의 하위 컴포넌트를 모아두는 폴더
  

# Router 실습
## 주소를 이동하는 2가지 방법
1. 선언적 방식 네비게이션
- router-link의 'to'속성으로 주소 전달

![image](https://user-images.githubusercontent.com/122726684/236980613-0bd5f875-b83c-4454-97d6-2693a1d18598.png)

2. 프로그래밍 방식 네비게이션
- 동적인 값을 사용하기 때문에 v-bind를 사용해야 정상적으로 작동

![image](https://user-images.githubusercontent.com/122726684/236980730-a01c059c-8cdf-4361-a45e-e95cb2608c15.png)

- Vue 인스턴스 내부에서 라우터 인스턴스에 `$router`로 접근 할 수 있음
- 다른 URL로 이동하려면 `this.$router.push`를 사용
  - history stack에 이동할 URL를 넣는 방식
  - historty stack에 기록이 남기 때문에 사용자가 브라우저에 뒤로 가기 버튼을 클릭하면 이전 URL로 이동할 수 있음

![image](https://user-images.githubusercontent.com/122726684/236981316-dbdcb3ce-f532-4a92-8577-7c70a72caed0.png)

## Dynamic Route Matching
- 동적 인자 전달
  - URL의 특정 값을 변수처럼 사용할 수 있음
- 예시:
  - HelloView.vue 작성 및 route 추가
  - route 추가할 때 동적 인자를 명시
  
![image](https://user-images.githubusercontent.com/122726684/236981734-10162628-abf6-4892-ab50-b8ef87fc3234.png)

- `$route.params`로 변수에 접근 가능

![image](https://user-images.githubusercontent.com/122726684/236981911-a495eb3e-5352-42ab-aa12-1d03bab55c06.png)

- 직접 사용하기 보다 data에 넣어서 사용하는 것을 권장
  
![image](https://user-images.githubusercontent.com/122726684/236982123-057e7b53-3a8c-4ece-b607-95ed8ca0fdb6.png)

### Dynamic Route Matching - 선언적 방식 네비게이션

![image](https://user-images.githubusercontent.com/122726684/236982295-50d319e5-8de5-4f37-ab33-4ac74dc18d2e.png)

### Dynamic Route Matching - 프로그래밍 방식 네비게이션

![image](https://user-images.githubusercontent.com/122726684/236982535-d9f1ad3a-854e-4591-9c2a-af314dbb2ad2.png)

## lazy-loading
- 모든 파일을 한 번에 로드하려고 하면 모든 걸 다 읽는 시간이 매우 오래 걸림
- 미리 로드하지 않고 특정 라우트에 방문 할때 매핑된 컴포넌트의 코드를 로드하는 방식을 활용할 수 있음
  - 최초에 로드하는 시간 빨라짐
  - 당장 사용하지 않을 컴포넌트는 먼저 로드하지 않는 것이 핵심
