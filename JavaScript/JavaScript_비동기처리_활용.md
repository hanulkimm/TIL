# 비동기 처리 활용하기

## AJAX
### 개념
- 비동기 통신을 이용하여 화면 전체를 새로고침 하지 않아도 서버로 요청을 보내고 데이터를 받아 화면의 일부분만 업데이트 가능
- 비동기 통신 웹 개발 기술을 AJAX 라고 함
- 비동기 웹 통신을 위한 라이브러리 중 하나가 Axios

### 특징
- 페이지 전체를 reload(새로 고침) 하지 않아도 수행되는 '비동기성'
- 서버의 응답에 따라 전체 페이지가 아닌 일부분만을 업데이트 할 수 있음
  - 페이지 새로 고침없이 서버에 요청
  - 서버로부터 응답을 받아 작업을 수행

# 비동기 적용하기
## 팔로우
### 사전 준비
- script block tag 영역 작성
  
![image](https://user-images.githubusercontent.com/122726684/234447620-0a1cdcc9-f7ea-4bd3-8064-5976dc33f18f.png)  

- axios CDN 작성

![image](https://user-images.githubusercontent.com/122726684/234447694-88f79f3f-dab6-4fee-a507-9f03b5f667c5.png)  

- form 요소 선택을 위해 id 속성 지정 및 선택 (불필요한 action과 method 속성 삭제)

![image](https://user-images.githubusercontent.com/122726684/234447794-e444343d-464a-49dc-9602-6f45553b39d2.png)

- 팔로우 (follow)

![image](https://user-images.githubusercontent.com/122726684/234447938-cc640e24-7f5c-4b9e-abdd-e3930a2f300c.png)

- form 요소에 이벤트 핸들러 작성 및 submit 이벤트 취소

![image](https://user-images.githubusercontent.com/122726684/234448232-4711a194-cde7-4c94-a164-1f5572d6e915.png)

- axios 요청 준비

![image](https://user-images.githubusercontent.com/122726684/234448430-97ff25ea-1e77-4955-868c-2ec163df0893.png)

### POST 요청을 보내기 위해 필요한 것
1. url에 작성할 user pk 작성하기

2. csrftoken 보내기
- 참고: https://docs.djangoproject.com/en/4.2/howto/csrf/  
- hidden 타입으로 숨겨져 있는 csrf 값을 가진 input 태그를 선택하기

![image](https://user-images.githubusercontent.com/122726684/234463588-574a9269-b9ae-4c3f-becd-82e7c8f4028b.png)

- AJAX로 csrftoken 보내기
  - axios 공식문서 확인하기, config 옵션이 django 공식문서에서 알려주는 옵션과 같은 지 확인

![image](https://user-images.githubusercontent.com/122726684/234463649-a972df7a-463a-4b1d-abba-868768c4e7dd.png)

### 팔로우
- 팔로우 버튼 토글하기 위해서는 현재 팔로우 상태 확인 필요
- axios 요청을 통해 받는 response 객체를 활용해 view 함수를 통해 팔로우 여부를 파악할 수 있는 변수를 담아 JSON 타입으로 응답하기
- 팔로우 여부 파악, JSON 응답

![image](https://user-images.githubusercontent.com/122726684/234475652-03a3d672-8d78-4026-b1f7-e1cedc30d5a9.png)

- 버튼 토글하기

![image](https://user-images.githubusercontent.com/122726684/234475774-85ab155e-f1ec-4bf6-9612-a4fbc162fb1a.png)