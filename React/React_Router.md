# Router

## Router 시작하기

```
npm install react-router-dom
```

## Router import

```js
// index.html
root.render(
  <React.StrictMode>
    <BrowserRouter> // 추가해주기
    <App />
    </BrowserRouter>
  </React.StrictMode>
);

// App.js
import {Routes, Route, Link, useNavigate, Outlet} from 'react-router-dom';

// navigate 사용
<Nav.Link onClick={()=>{navigate('/')}}>Home</Nav.Link>
<Nav.Link onClick={()=>{navigate('/detail')}} >Detail</Nav.Link>

// 여기 안에 route 적어주기
<Routes>
  <Route path="/" element={}/>

  // nested routes
  <Route path='/about' element={<About/>}>
    <Route path='member' element={<div>멤버임</div>}/>
    <Route path='location' element={<About/>}/>
  </Route>

  // params 넘겨주기
  <Route path="/detail/:id" element={<Detail shoes={shoes}/>}/>
  // 여러 개 넘겨주기도 가능
  <Route path="/detail/:id/:name" element={<Detail shoes={shoes}/>}/>


</Routes>


// Detail.js
function Detail(props) {

  let {id} = useParams();
  // 목록의 id로 접근하는 방법
  let shoe = props.shoes.find((shoe)=> {
    return shoe.id==id; // ===이면 안됨!!
  })

}

```
