## local storage

### 기본 문법
```js
localStorage.setItem('name':'data');
localStorage.getItem('name');
localStorage.removeItem('name');
```

### array/object 자료 저장
```js
localStorage.setItem('obj', JSON.stringify({name:'kim'}))
let a = localStorage.getItem('obj')
let a = JSON.parse(a)
```