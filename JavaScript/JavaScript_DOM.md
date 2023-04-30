# DOM
## 관련 개념
- 브라우저 APIs: 웹 브라우저에 내장된 API로 웹 브라우저가 현재 컴퓨터 환경에 관한 데이터를 제공하거나 오디오를 재생하는 등 여러가지 유용하고 복잡한 일을 수행할 수 있게 함
  - 종류 : DOM
- JavaScript는 DOM API를 통해 html과 css를 동적으로 수정하고 사용자 인터페이스를 업데이트 하는 일에 가장 많이 쓰임
- DOM: 문제 객체 모델(Document Object Model)
  - 문서의 구조화된 표현을 제공하며 HTML 문서를 구조화하여 각 요소를 객체로 취급
  
## DOM 기본 구조
 ![image](https://user-images.githubusercontent.com/122726684/233269597-f3bd661e-2df8-4ffa-b034-8ea938310226.png)

## DOM 조작
- 조작 순서: 선택(select) -> 조작 (manipulation)

## 선택 관련 메서드
- `document.querySelector(selector)`
  - 제공한 선택자와 일치하는 element 한 개 선택
  - 제공한 CSS selector 조건 만족하는 첫 번째 element 객체 반환 (없다면 null 반환)
  - '#' 는 id, '.' 는 class
- `document.querySelectorAll(selector)`
  - 제공한 선택자와 일치하는 여러 element를 선택
  - 매칭 할 하나 이상의 셀럭터를 포함하는 유효한 CSS selector를 인자(문자열)로 받음
  - 제공한 CSS selector를 만족하는 NodeList를 반환
- 예시:
```html
<body>
  <h1 id="title">DOM 조작</h1>
  <p class="text">querySelector</p>
  <p class="text">querySelectorAll</p>

  <ul>
    <li>Javascript</li>
    <li>Python</li>
  </ul>
  
  <script>
    document.querySelector('#title') 
    // <h1 id="title">DOM 조작</h1>
    document.querySelector('.text') 
    // <p class="text">querySelector</p>
    document.querySelectorAll('.text') 
    // NodeList(2) [p.text, p.text]
    document.querySelectorAll('body > ul > li') 
  </script>
</body>
```

## 조작 관련 메서드 
- 생성: `document.createElement(tagName)` 
  - 작성한 tageName의 HTML 요소를 생성하여 반환
- 입력: `___.innertext`
  - 사람이 읽을 수 있는 요소만 남김
- 추가 : `Node.appendChild()`
  - 한 Node를 특정 부모 Node의 자식 NodeList 중 마지막 자식으로 삽입
  - 한번에 오직 하나의 Node만 추가할 수 있음
  - 추가된 Node 객체를 반환
- 삭제 : `Node.removeChild()`
  - DOM에서 자식 Node를 제거
  - 제거된 Node를 반환
- 예시
```html
<body>
  <div></div>
<script>
  // 태그 생성
  const title = document.createElement('h1')
  // 태그안에 컨텐츠를 작성하고
  title.innertext = 'DOM조작'
  // 부모 div 태그를 가져와서
  const div = document.createElement('div')
  // div 태그의 자식 요소로 추가
  div.appendChild(title)
  // div의 h1 요소 삭제
  div.removeChild(title)
</script>
</body>
```
- 새롭게 생성한 Node가 아닌 이미 문서에 존재하는 Node를 다른 Node의 자식으로 삽입하는 경우, 위치를 이동
```html
<body>
  <h1>과일 목록</h1>
  <ul id="fruits">
    <li id="apple">apple</li>
  </ul>
  <h1>야채 목록</h1>
  <ul id="fruits">
    <li id="banana">Banana</li>
    <li id="cucumber">Cucumber</li>
  </ul>

  <script>
    const fruitsList = document.querySelector('#fruits')
    const banana = document.querySelector('#banana')
    fruitsList.appendChild(banana)
  </script>
</body>
```
### 속성 조회 및 설정
- `element.getAttribute(attributeName)`
  - 해당 요소의 지정된 값(문자열)을 반환
  - 인자(attributeName)는 값을 얻고자 하는 속성의 이름
- `element.setAttribute(attributeName)`
  - 지정된 요소의 값을 설정
  - 속성이 이미 존재하면 값을 갱신, 존재하지 않으면 지정된 이름과 값으로 새 속성 추가 
- 예시:  
![image](https://user-images.githubusercontent.com/122726684/233268696-a5b80145-bb9d-4db3-9465-f890b319e641.png)

### 예시
```html
<style>
  .red {
    color: red;
  }

  .big {
    font-size: 32px;
  }
</style>
<body>
  <h1>selector test</h1>

  <button id="event-button">커져라!</button>

  <ul id="list">
    <li class="red">apple</li>
    <li>orange</li>
    <li id="banana">banana</li>
    <li>grape</li>
    <li class="red">strawberry</li>
  </ul>

  <script>
    // strawberry 아래에 새로운 과일 하나 추가
    const mango = document.createElement("li")
    mango.innerText = '망고'
    const parent = document.querySelector('ul')
    parent.appendChild(mango)
    // apple 위에 새로운 과일 하나 추가
    const pineapple =document.createElement('li')
    pineapple.innerText = '파인애플'
    parent.prepend(pineapple)
    // orange 와 banana 사이에 새로운 과일 하나 추가
    const kiwi = document.createElement('li')
    kiwi.innerText = "kiwi"
    const banana = document.querySelector('#banana')
    parent.insertBefore(kiwi, banana)

    // class가 red인 노드 모두 삭제
    const reds = document.querySelectorAll('.red')
    reds.forEach(element=> {
      element.remove()
    })

    // 모든 li 태그 글자 키우기
    const liTags = document.querySelectorAll('li')
    liTags.forEach(element => {
      element.classList.add('big')
    });

    // 버튼을 누르면 이벤트 실행하기
    const button = document.querySelector('#event-button')
    button.addEventListener('click', () => {
      changeFont()
    })

    function changeFont() {
      const liTags = document.querySelectorAll('li')
      liTags.forEach(element => {
        element.classList.add('big')
      })
    }

  </script>
</body>
```
```html
<body>
  <ul id="fruits-list">
  </ul>

<script>
  const fruits = ['apple', 'banana', 'orange']
  fruits.forEach(fruit => {
    const li = document.createElement('li')
    li.innerText = fruit
    document.querySelector('ul').appendChild(li)
  });
</script>
</body>
```