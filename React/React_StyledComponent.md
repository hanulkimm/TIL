## Styled components

### 시작하기
```
npm install styled-components
```

### 사용하기

```js
// styled components
let YelloBtn = styled.button`
  background: yellow;
  color: black;
  padding: 10px;
`;
let Box = styled.div`
  background: grey;
  padding: 20px;
`;

function Detail(props) {
  return (
    <div className="container">
      <Box>
        <YelloBtn>버튼</YelloBtn>
      </Box>
    </div>
  );
}
```

### props로 재활용하기
```js
let YelloBtn =  styled.button`
  background: ${props=>props.bg};
  color: ${props=>props.bg=='blue'?'white':'black'};
  padding: 10px;
`

function Detail(props) {
  return(
    <Box>
      <YelloBtn bg="blue">버튼</YelloBtn>
      <YelloBtn bg="yellow">버튼</YelloBtn>
  </Box>
  )
}
```

### 장점
1. CSS 파일 오픈 필요없이 JS파일에 바로 스타일링
2. 스타일이 다른 JS 파일에 오염되지 않음
- 원래는 오염됨, 이것을 방지하기 위해서는 css파일에 .modules.css 로 이름 지으면 됨
- ex.App.modules.css
3. 페이지 로딩시간 단축

### 단점
1. js 파일이 길어지고 복잡해짐
2. js 파일 간 중복 디자인 --> import하면 css와 다를 게 없음
3. 협업 시 불편할수도