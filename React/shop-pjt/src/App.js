import { Button, Navbar, Container, Nav, Row, Col } from 'react-bootstrap';
import './App.css';
import puppyImg from './img/puppy.png';
import { useState } from 'react';
import data from './data';
import {Routes, Route, Link, useNavigate, Outlet} from 'react-router-dom';
import Detail from './routes/Detail';

function App() {

  let [shoes, setShoes] = useState(data);
  let navigate = useNavigate();

  return (
    <div className="App">

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
                  shoes.map((shoe)=>{
                    return(
                      <Shoe shoe={shoe} />
                    )
                  })
                }
              </div>
            </div>
          </>
        }/>

        <Route path='/about' element={<About/>}>
          <Route path='member' element={<div>멤버임</div>}/>
          <Route path='location' element={<About/>}/>
        </Route>


        <Route path='/detail' element={<Detail/>}/>
        <Route path='/event' element={<Element/>}>
          <Route path='one' element={<div>첫 주문시 서비스</div>}/>
          <Route path='two' element={<div>생일 기념 쿠폰</div>}/>
        </Route>
        {/* <Route path='/about' element={<About/>}/>
        <Route path='/about/member' element={<About/>}/>
        <Route path='/about/location' element={<About/>}/> */}
      </Routes>

    </div>
  );
}

function Element() {
  return(
    <div>
      <h4>오늘의 이벤트</h4>
      <Outlet></Outlet>
    </div>
  )
}

function About() {
  return(
    <div>
      <h4>회사 정보임</h4>
      <Outlet></Outlet>
    </div>
  )
}


function Shoe(props) {
  return(
    <div className="col-md-4">
      <img src={`https://codingapple1.github.io/shop/shoes${props.shoe.id+1}.jpg`} width="80%" alt="" />
      <h4>{props.shoe.title}</h4>
      <p>{props.shoe.content}</p>
    </div>
  )
}



export default App;