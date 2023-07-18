## 서버와 통신 AJAX

### axios 설치
```
npm install axios
```

### AJAX 요청하기 
```js
// GET 요청보내기
<button onClick={()=>{
  axios.get(`https://codingapple1.github.io/shop/data${clickBtn}.json`)
  .then((res)=>{
    // console.log(res.data)
    let copy = [...shoes, ...res.data]
    setShoes(copy)
  })
  

}} >더보기</button>

// POST 요청
axois.post('URL', {name: 'kim'})
```

### 동시에 AJAX 요청 보내기
```js
Promise.all([axois.get('url1'),axois.get('url2') ])
```

### fetch
- json으로 받아오기 때문에 다시 object/array로 변환해주어야 함


### AJAX 요청 받은 데이터를 html 렌데링할 때 에러나는 경우
- AJAX 요청보다 html렌더링이 빨라서
- if문 같은 거 사용해서 처리하기