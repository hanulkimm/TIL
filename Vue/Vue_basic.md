# Basic of Syntax
## Text Interpolation
- 가장 기본적인 바인딩(연결) 방법
- 중괄호 2개로 표시
- 일반 텍스트로 표현

![image](https://user-images.githubusercontent.com/122726684/235412997-aae4acb5-a858-49ef-8485-a5627913421c.png)
## Raw HTML
- v-html directive을 사용하여 data와 바인딩

![image](https://user-images.githubusercontent.com/122726684/235412978-9df4e438-a684-42ab-8adb-2b6f34ef4b9b.png)

# Directives
## 기본 구성
![image](https://user-images.githubusercontent.com/122726684/235413516-395d093b-70a1-441c-9f46-4d6de9420889.png)

- v 접두사가 있는 특수 속상에는 값을 할당 할 수 있음
- directive의 역할은 표현식의 값이 변경될 때 반응적으로 DOM에 적용하는 것
- `:`을 통해 전달 인자를 받을 수 있음

## v-text
- template interpolation과 함께 가장 기본적인 바인딩 방법
- {{}} 와 비슷한 역할
```html
<div id="app">
  <p v-text="message"></p>
  <!-- 같음 -->
  <p>{{message}}</p>
</div>

<script>
  const app = new Vue({
    el:'#app',
    data :{
      message : 'Hello!',
    }
  })
</script>
```
## v-html
- RAW HTML을 표현할 수 있는 방법
- 단, 사용자가 입력하거나 제공하는 컨텐츠에는 절대 사용 금지
```html
<div id="app">
  <p v-html="html"></p>
</div>

<script>
  const app = new Vue({
    el:'#app',
    data :{
      html: '<a href="https://google.com">GOOGLE</a>'
    }
  })
</script>
```

## v-show
- 표현식에 작성된 값에 따라 element를 보여 줄 것인지 결정
  - boolean 값이 변경 될 때 마다 반응
- 대상 element의 display 속성을 기본 속성과 none으로 toggle
- 요소 자체는 항상 DOM에 렌더링 됨
- 예시:
```html
<div id="app2">
  <p v-show="isActive">보이니?</p>
</div>
<script>
  const app2 = new Vue({
    el : '#app2',
    data : {
      isActive : false
    }
  })
</script>
```
- 바인딩된 isActive의 값이 false이므로 첫 방문 시 p tag는 보이지 않음
- vue dev tools에서 isActive 변경 시 화면에 출력
- 화면에서 사라졌을 뿐, DOM에는 존재한다

## v-if
- v-show와 사용 방법은 동일
- isActive의 값이 변경될 때 반응
- 단, 값이 false인 경우 DOM에서 사라짐
```html
<div id="app2">
  <p v-show="isActive">보이니?</p>
  <p v-if="isActive">보이냥?</p>
</div>
<script>
  const app2 = new Vue({
    el : '#app2',
    data : {
      isActive : false
    }
  })
</script>
```
## v-show 와 v-if
### v-show
- 표현식 결과와 관계없이 렌더링 되므로 초기 렌더링에 필요한 비용은 더 높을 수 있음
- display 속성 변경으로 표현 여부를 판단하므로 렌더링 후 toggle 비용은 적음
### v-if
- 표현식 결과가 false인 경우 렌더링 조차 되지 않으므로 초기 렌더링 비용은 v-show보다 낮을 수 있음
- 표현식 값이 자주 변경되는 경우 잦은 재 렌더링으로 비용이 증가할 수 있음

## v-for
- `for .. in ..` 형식으로 작성
- 반복한 데이터 타입에 모두 사용 가능
- index와 함께 출력하고자 한다면 (char, index)형태로 사용 가능
- 객체, 배열 역시 문자열과 동일하게 사용 가능 (dot notation으로 접근)
- 
```html
<div id="app3">
  <!-- 문자열 -->
  <div v-for="(char, index) in myStr">
    <p>{{index}}번째 문자열 {{char}}</p>
  </div>
  <!-- 배열 -->
  <div v-for="(item, index) in myArr" : key="`array-${index}`">
    <p>{{index}} 번째 아이템 {{item}}</p>
  </div>
  <!-- 객체 -->
  <div v-for="(value, key) in myObj" : key="key">
    <p>{{key}}:{{value}}</p>
  </div>
</div>
<script>
  const app = new Vue({
    el:'#app3',
    data:{
      myStr:'Hello, World!'
      myArr: ['python', 'django', 'vue.js'],
      myObj : {
          name: 'Hanul',
          age: 24
        },
    }
  })
</script>
```

## v-on
- `:`을 통해 전달받은 인자를 확인
- 값으로 JS 표현식 작성
- addEventListener의 첫번째 인자와 동일한 값들로 구성
- 대기하고 있던 이벤트가 발생하면 할당된 표현식 실행
- method 통한 data 조작 가능
- `@` shortcut 제공
```html
<div id="app">
    <button v-on:click="number++">
    <!-- <button @click="number++"> -->
      increase Number
    </button>
    <p>{{number}}</p>
  </div>

  <script>
    const app = new Vue({
      el : '#app',
      data: {
        number:0
      }
    })
  </script>
```

## v-bind
- HTMl 기본 속성에 Vue data를 연결
- class의 경우 다양한 형태로 연결 가능
  - 조건부 바인딩: `{'class name':'조건 표현식'}`
- `:` shortcut 제공
```html
<div id="app">
    <a v-bind:href="url">Google</a>
    <!-- shortcut -->
    <a :href="url">Google</a>
  </div>

  <script>
    const app = new Vue({
      el : '#app',
      data: {
        url:'https://www.google.com/'
      }
    })
  </script>
```
## v-model
- vue instance와 DOM의 양방향 바인딩
- vue data 변경 시 v-model로 연결된 사용자 입력 element에도 적용
```html
<div id="app">
    <h3>{{message}}</h3>
    <input v-model="message" type="text">
  </div>

  <script>
    const app = new Vue({
      el : '#app',
      data: {
        message:''
      }
    })
  </script>
```

# Vue advanced
## computed
- vue instance가 가진 options 중 하나
- computed 객체에 정의한 함수를 페이지가 최초로 렌더링 될 때 호출하여 계산
  - 계산 결과가 변하기 전까지 함수를 재호출하는 것이 아닌 계산된 값을 반환
## methods 와 computed
### methods
- 호출될 때 마다 함수 실행
- 같은 결과여도 매번 새롭게 계산
### computed
- 함수의 종속 대상의 변화에 따라 계산 여부가 결정됨
- 종속 대상이 변하지 않으면 항상 저장된 값 반환

## watch
- 특정 데이터의 변화를 감지하는 기능
- watch 객체 정의 --> 감시할 대상 data 지정 --> data가 변할 시 실행 할 함수 정의
```html
<div id="app">
    <button @click="number++">{{number}}</button>
  </div>

  <script>
    const app = new Vue({
      el : '#app',
      data: {
        number:0
      },
      watch:{
        number:function(val, oldVal){
          console.log(val, oldVal)
        }
      }
    })
  </script>
```
## filters
- 텍스트 형식화를 적용할 수 있는 필터
- interpolation 혹은 v-bind를 이용할 때 사용 가능
- 