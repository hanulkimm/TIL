import { Button, Navbar, Container, Nav, Row, Col } from 'react-bootstrap';
import './App.css';
import puppyImg from './img/puppy.png';
import { useState } from 'react';
import data from './data';

function App() {

  let [shoes, setShoes] = useState(data);

  return (
    <div className="App">
      <Navbar bg="light" data-bs-theme="light">
        <Container>
          <Navbar.Brand href="#home">개밥바라기</Navbar.Brand>
          <Nav className="me-auto">
            <Nav.Link href="#home">Recipes</Nav.Link>
            <Nav.Link href="#features">Streaming</Nav.Link>
            <Nav.Link href="#pricing">Community</Nav.Link>
          </Nav>
        </Container>
      </Navbar>
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
    
    </div>
  );
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