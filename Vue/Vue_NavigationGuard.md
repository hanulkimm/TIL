# Navigation Guard
## 개념
- vue router를 통해 특정 URL에 접근할 때, 다른 url로 redirect하거나 해당 URL로의 접근을 막는 방법
- 예시: 사용자의 인증 정보가 없으면 특정 페이지에 접근하지 못하게 함
## 종류
- 전역 가드: 애플리케이션 전역에서 등장
- 라우터 가드: 특정 URL에서만 동작
- 컴포넌트 가드: 라우터 컴포넌트 안에 정의

## 전역 가드
- 다른 url 주소로 이동할 때 항상 실행
- router/index.js에 `router.beforeEach()`를 사용하여 설정
- 콜백 함수의 값으로 3개의 인지를 받음
  - to: 이동할 URL 정보가 담긴 Route 객체
  - from: 현재 URL 정보가 담긴 Route 객체
  - next: 지정한 URL로 이동하기 위해 호출하는 함수
    - 콜백 함수 내부에서 반드시 한 번만 호출되어야 함
    - 긱본적으로 to에 해당하는 URL로 이동
- URL이 변경되어 화면이 전환되기 전 router.beforeEach()가 호출됨
  - 화면이 전환되지 않고 대기 상태가 됨
- 변경된 URL로 라우팅하기 위해서는 next()를 호출해줘야 함
  - next()가 호출되기 전까지 화면이 전환되지 않음

### 실습: login 여부에 따른 라우팅 처리
- login이 되어 있지 않다면 login 페이지로 이동하는 기능 추가

![image](https://github.com/hanulkimm/codingtestprep/assets/122726684/38fe9d04-b6aa-4b9e-8afc-45c13afea4b7)

- LoginView에 대한 라우터 링크 추가

![image](https://github.com/hanulkimm/codingtestprep/assets/122726684/7161d517-4549-4d5f-88fa-acc29d5e5c7c)

- HelloView에 로그인을 해야만 접근이 가능하도록 만들기

![image](https://github.com/hanulkimm/codingtestprep/assets/122726684/4051b1d7-87f7-4d84-befb-ea241a84a228)

![image](https://github.com/hanulkimm/codingtestprep/assets/122726684/bd98cf1f-b681-4d1f-8d0d-25dceb274a9f)

- View들이 여러 개라면 반대로 login하지 않아도 되는 페이지들을 모아 둘 수도 있음

![image](https://github.com/hanulkimm/codingtestprep/assets/122726684/ef1ba35e-ee08-4f4c-9ca9-dca58453e639)

## 라우터 가드
- 전체 route가 아닌 특정 route에 대해서만 가드를 설정하고 싶을 때 사용
- `beforeEnter()`
  - route에 진입했을 때 실행됨
  - 라우터를 등록한 위치에 추가
  - 단 매개변수, 쿼리, 해시 값이 변경될 때는 실행되지 않고 다른 경로에서 탐색할 때만 실행됨
  - 콜백 함수는 to, form, next를 인자로 받음

### 실습: login여부에 따른 라우팅 처리
- 이미 로그인되어 있는 경우 HomeView로 이동하기

![image](https://github.com/hanulkimm/codingtestprep/assets/122726684/832ff89c-ec65-43a9-8907-203ac6517968)

## 컴포넌트 가드
- 특정 컴포넌트 내에서 가드를 지정하고 싶을 때 사용
- `beforeRouteUpdate()`
  - 해당 컴포넌트를 렌더링하는 경로가 변경될 때 실행
### Params 변화 감지
- `beforeRouteUpdate()`를 사용해서 userName을 이동할 params에 있는 userName으로 재할당

## 404 Not Found
- 사용자가 요청한 리소스가 존재하지 않을 때 응답

![image](https://github.com/hanulkimm/codingtestprep/assets/122726684/dd02c5f4-faae-4e58-abb6-846a1763d5f3)

- 모든 경로에 대해서 404page로 redirect 하기
  - 기존에 명시한 경로가 아닌 모든 경로가 404 page로 redirect 됨
  - routes의 최하단부에 작성해야 함
  
![image](https://github.com/hanulkimm/codingtestprep/assets/122726684/946f6f4c-b816-49e2-a528-83fa3b0c5930)

### 형식을 유효하지만 특정 리소스를 찾을 수 없는 경우
- Dog API 이용하여 동적 인자로 강아지 품종을 전달해 품종에 대한 랜덤 이미지를 출력하는 페이지 만들기

- axios 설치하고 DogView 컴포넌트 작성, routes에 등록하기

![image](https://github.com/hanulkimm/codingtestprep/assets/122726684/2378fd9a-b4e8-4069-a634-06c1b1b83d10)

- axios 로직 작성

![image](https://github.com/hanulkimm/codingtestprep/assets/122726684/e0e5ce25-be53-48b6-9bd5-faf615b48acf)

- axios 요청이 오는 중 동작하고 있음을 표현하기 위한 로딩 메시지 정의

![image](https://github.com/hanulkimm/codingtestprep/assets/122726684/ee68dbf8-d59d-4fac-b35b-732e861a7983)

- axios 요청이 실패할 경우 자료가 없을 표현하기

![image](https://github.com/hanulkimm/codingtestprep/assets/122726684/2efd7ce6-baee-4fff-8582-ded3642b75fb)

- 아니면 axios 요청이 실패할 경우 404 페이지로 이동 시킬 수도 있음

![image](https://github.com/hanulkimm/codingtestprep/assets/122726684/57378782-0c5a-479e-a418-d4293b9e49df)