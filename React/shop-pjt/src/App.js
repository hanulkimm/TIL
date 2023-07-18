import { Button, Navbar, Container, Nav, Row, Col } from 'react-bootstrap';
import './App.css';
import puppyImg from './img/puppy.png';
import { useEffect, useState } from 'react';
import data from './data';
import {Routes, Route, Link, useNavigate, Outlet} from 'react-router-dom';
import Detail from './routes/Detail';
import axios from 'axios';

function App() {

  let [shoes, setShoes] = useState(data);
  let navigate = useNavigate();
  let [input, setInput] = useState(0);
  let [clickBtn, setClickBtn] = useState(1);
  let [showBtn, setShowBtn] = useState(true);
  useEffect(()=>{
    if (isNaN(input)) {
      alert('놉')
    }
  }, [input])

  return (
    <div className="App">
        <input type="text" onChange={(e)=>setInput(e.target.value)}/>
      <Navbar bg="light" data-bs-theme="light">
        <Container>
          <Navbar.Brand href="#home">개밥바라기</Navbar.Brand>
          <Nav className="me-auto">
            {/* <Link to="/">홈</Link>
            <Link to="/detail">상세페이지</Link> */}
            <Nav.Link onClick={()=>{navigate('/')}}>Home</Nav.Link>
            <Nav.Link onClick={()=>{navigate('/detail')}} >Detail</Nav.Link>
          </Nav>
        </Container>
      </Navbar>

      
      <Routes>
        <Route path='/' element={
          <>
            <div className='main-bg' style={{backgroundImage: 'url('+puppyImg+')'}}></div>
            <div className="container">
              <div className="row">
                {
                  shoes.map((shoe,i)=>{
                    return(
                      <Shoe shoe={shoe} key={i} />
                    )
                  })
                }
              </div>
            </div>
            
            {
              showBtn 
              ? <button onClick={()=>{
                  setClickBtn(clickBtn+1)
                  if (clickBtn==3) {
                    setShowBtn(false)
                  }
                  axios.get(`https://codingapple1.github.io/shop/data${clickBtn}.json`)
                  .then((res)=>{
                    // console.log(res.data)
                    let copy = [...shoes]
                    let newCopy = copy.concat(res.data)
                    setShoes(newCopy)
                  })
                

                }} >더보기</button>
              : null
            }
           
          </>
        }/>

        <Route path="/detail/:id" element={<Detail shoes={shoes}/>}/>

      </Routes>

    </div>
  );
}


function Shoe(props) {
  return(
    <div className="col-md-4">
      <img src={`https://codingapple1.github.io/shop/shoes${props.shoe.id+1}.jpg`} width="80%" alt="" />
      {/* <img src='https://recipe1.ezmember.co.kr/cache/recipe/2019/11/16/fc6e5e42d13ae19e8c8a67f4d15259211.png' width="80%" alt="" /> */}
      <h4>{props.shoe.title}</h4>
      <p>{props.shoe.content}</p>
    </div>
  )
}


export default App;