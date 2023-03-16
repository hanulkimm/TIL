# Form & Data

## Sending Form data (Client)
### HTML <form> 요소
- 데이터가 전송되는 방법을 정의
- 사용자로부터 할당된 데이터를 서버로 전송하는 역할을 담당
- 데이터를 어디(action)로 어떤 방식(method)으로 보낼지
- 
### HTML Form 속성
1. action
- 입력 데이터가 전송될 url을 지정
- 반드시 유효한 url이어야 함
- 지정하지 않으면 현재 form이 있는 페이지의 url로 보내짐

2. method
- 데이터를 어떻게 보낼 것인지 정의
- 입력 데이터의 HTTP request methods를 지정
- HTML form 데이터는 오직 2가지 방식으로 전송
  - GET 방식과 POST 방식

### HTML <input> 요소
- 사용자로부터 데이터 입력 받기 위해 사용
- 'type'속성에 따라 동작 방식이 달라짐 (기본값은 text)
- 핵심 속성 : name

### HTML <input> 속성 : name
- name: form를 통해 데이터를 제출(submit)했을 때 name 속성에 설정된 값을 서버로 전송하고, 서버는 name 속성에 설정된 값을 통해 사용자가 입력한 데이터 값에 접근할 수 있음
- 서버에 전달하는 파라미터로 매핑하는 것

### HTTP request methods
- HTTP란? HTML 문서와 같은 리소스들을 가져올 수 있도록 해주는 프로토콜
- 웹에서 이루어는 모든 데이터 교환의 기초
- HTTP는 주어진 리소스가 수행 할 원하는 작업을 나타내는 method를 정의
- HTTP method 종류: GET, POST, PUT, DELETE

### HTTP request methods : GET
- 서버로부터 정보를 조회하는 데 사용
- 데이터를 가져올 때만 사용해야 함
- 데이터를 서버에 전송할 때 query string parameters를 통해 전송
  - 데이터는 URL에 포함되어 서버로 보내짐
### Query String Parameters
- 사용자가 입력 데이터를 전달하는 방법 중 하나로, url 주소에 데이터를 파라미터를 통해 넘기는 것
- key=value 쌍으로 구성되며 여러 쌍인 경우 & 로 연결
- 예시: http://host:port/path?key=value&key=value

# Retrieving the Data (Server)
- 데이터 가져오기
- 데이터는 URL에 포함되어 서버로 보내짐

# 예시
```html
  <form action="https://www.google.com/search" method="GET">
    <label for="nickname">nickname: </label>
    <input type="text" name="query" id="nickname">
    <input type="submit">

  </form>
```