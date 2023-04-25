# 동기와 비동기 처리

## 동기
- 모든 일을 순서대로 하나씩 처리하는 것
- 이전 작업이 끝나면 다음 작업을 시작함
- 요청과 응답을 동기식으로 처리한다면 요청을 보내고 응답이 올 때까지 기다렸다가 다음 로직을 처리
- 지금까지 작성했던 python 코드는 모두 동기식

## 비동기
- 작업을 시작한 후 결과를 기다리지 않고 다음 작업을 처리하는 것 (병렬적 수행)
- 사건이 필요한 작업들은 요청을 보낸 뒤 응답이 빨리 오는 작업부터 처리
- 예시: gmail에서 메일 전송을 누르면 목록 화면에서 전환되지만 실제로 메일을 보내는 작업은 병렬적으로 뒤에서 처리됨

### 비동기(Asynchronous) 사용하는 이유
- 사용자 경험
- 예시: 아주 큰 데이터를 불러온 뒤 실행되는 앱이 있을 때 동기로 처리한다면 데이터를 모두 불러온 뒤에야 앱의 실행 로직이 수행되므로 사용자들은 마치 앱이 멈춘 것과 같은 경험을 겪게 됨
- 즉, 동기식 처리는 특정 로직이 실행되는 동안 다른 로직 실행을 차단하기 때문에 마치 프로그램이 응답하지 않는 듯한 사용자 경험을 만들게 됨
- 비동기로 처리한다면 먼저 처리되는 부분부터 보여줄 수 있으므로, 사용자 경험에 긍정적인 효과를 볼 수 있음

## JavaScript의 비동기 처리
- JavaScript는 Single Thread 언어:  JavaScript는 한 번에 하나의 일만 수행할 수 있는 Single Thread 언어로 동시에 여러 작업을 처리할 수 없음
  - 하나의 작업을 요청한 순서대로 처리할 수 밖에 없다
- JavaScript Runtime: 특정 언어가 동작할 수 있는 환경을 런타임이라 함
  - JS에서 비동기와 관련된 작업은 브라우저 또는 node 환경에서 처리

### 비동기 처리 동작 방식 (브라우저 환경)
1. 모든 작업은 Call Stack(LIFO)으로 들어간 후 처리한다.
2. 오래 걸리는 작업이 Call Stack으로 들어오면 Web API로 보내 별도로 처리하도록 한다.
3. Web API에서 처리가 끝난 작업들은 곧바로 Call Stack으로 들어가지 못하고 Task Queue(FIFO)에 순서대로 들어간다.
4. Event Loop가 Call Stack이 비어있는 것을 계속 체크하고 Call Stack이 빈다면 Task Queue에서 가장 오래된(가장 앞에 있는) 작업을 Call Stack으로 보낸다.

### 비동기 처리 동작 요소
1. Call Stack
- 요청이 들어올 때 마다 순차적으로 처리하는 Stack(LIFO)
- 기본적으로 JS의 Single Thread 작업 처리
2. Web API
- JS 엔진이 아닌 브라우저에서 제공하는 runtime 환경
- 시간이 소요되는 작업을 처리
3. Task Queue
- 비동기 처리된 Callback 함수가 대기하는 Queue(FIFO)
4. Event Loop
- Call Stack과 Task Queue를 지속적으로 모니터링
- Call Stack이 비어 있는지 확인 후 비어 있다면 Task Queue에서 대기 중인 오래된 작업을 Call Stack으로 Push

# Axios
## 개념
- JS의 HTTP 웹 통신을 위한 라이브러리
- 확장 가능한 인터페이스와 쉽게 사용할 수 있는 비동기 통신 기능을 제공
- node 환경은 npm을 이용해서 설치 후 사용할 수 있고 브라우저 환경은 CDN을 이용해서 사용할 수 있음

## 기본 구조
![image](https://user-images.githubusercontent.com/122726684/234150522-8a4a71c0-2833-4023-aa98-901cb39164e9.png)

### 예시: 고양이 사진 가져오기 (비동기)
```html
<body>

  <button>야옹아 이리온</button>

  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script>
      console.log('고양이는 야옹')
      const catImageSearchURL = 'https://api.thecatapi.com/v1/images/search'
      const btn = document.querySelector('button')
      btn.addEventListener('click', function(event) {
        axios.get(catImageSearchURL)
          .then((response) => {
            // console.log(response)
            // console.log(response.data)
            // console.log(response.data[0].url)
            imgElem = document.createElement('img')
            imgElem.setAttribute('src',response.data[0].url)
            document.body.appendChild(imgElem)
          })
          .catch((error) => {
            console.log('실패했다옹')
          })
  
        console.log('야옹야옹')

      })

  </script>
  
</body>
```

# Callback 과 Promise
## 비동기 처리의 단점
- Web API로 들어오는 순서가 아니라 작업이 완료되는 순서에 따라 처리함
- 코드의 실행 순서가 불명확하다는 단점이 있음
- 실행 결과를 예상하면서 코드를 작성할 수 없게 함

## 콜백 함수 (Callback Function)
- 연쇄적으로 발생하는 비동기 작업을 순차적으로 동작할 수 있게 함
- 보통 어느 기능의 실행 결과를 받아서 다른 기능을 수행하기 위해 많이 사용하는데 이 과정을 작성하다 보면 비슷한 패턴이 계속 발생하게 됨
- 콜백 지옥: 비동기 처리를 위한 콜백을 작성할 때 마주치는 문제
  - 코드의 가독성을 해치고 유지 보수가 어려워짐
  
## 프로미스 (Promise)
- Callback Hell 문제를 해결하기 위해 등장한 비동기 처리를 위한 객체
- 비동기 작업의 완료 또는 실패를 나타내는 객체
- Promise 기반의 클라이언트가 바로 이전에 사용한 Axios 라이브러리
  - 성공에 대한 약속 then()
  - 실패에 대한 약속 catch()
### then & catch
- then(callback) :
  - 요청한 작업이 성공하면 callback 실행
  - callback은 이전 작업의 성공 결과를 인자로 전달 받음
- catch(callback)
  - then()이 하나라도 실패하면 callback 실행
  - callback은 이전 작업의 실패 객체를 인자로 전달 받음
- then과 catch 모두 항상 promise 객체를 반환
  - 계속 chaining 할 수 있음
- axios로 처리한 비동기 로직이 항상 promise 객체 반환

![image](https://user-images.githubusercontent.com/122726684/234158023-2f59c9b9-dc78-436b-93ce-fad77f80debd.png)

### Promise 특징
1. call back함수는 JS의 Event Loop가 현재 실행 중인 Call Stack을 완료하기 이전에는 절대 호출되지 않음, Promise callback 함수는 Event Queue에 배치되는 엄격한 순서로 호출됨
2. 비동기 작업이 성공하거나 실패한 뒤에 .then() 메서드를 이용
3. .then() 을 여러 번 사용하여 여러 개의 callback 함수를 추가할 수 있음 (Chaining)
  - 각각의 callback은 주어진 순서대로 하나하나 실행하게 됨
  - chaining은 promise의 가장 뛰어난 장점
  