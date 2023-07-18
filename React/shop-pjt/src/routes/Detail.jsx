import { useContext, useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import styled from 'styled-components';
import {Nav, Tab} from 'react-bootstrap'
import {Context1} from './../App.js'
import { useDispatch, useSelector } from "react-redux";
import { addItem } from "../store.js";
// import './../App.css'

// styled components
let YelloBtn =  styled.button`
  background: ${props=>props.bg};
  color: ${props=>props.bg=='blue'?'white':'black'};
  padding: 10px;
`
let Box = styled.div`
  background: grey;
  padding: 20px;
`

function Detail(props) {

  let state = useSelector((state)=>state)
  let dispatch = useDispatch();
  console.log(state.info)
  
  let {stock, shoes} = useContext(Context1);

  let [count, setCount] = useState(0);
  let {id} = useParams();
  let shoe = props.shoes.find((shoe)=> {
    return shoe.id==id; // ===이면 안됨!! 
  })

  let [alert, setAlert] = useState(true);
  let [tab, setTab] = useState(0);

  useEffect(()=>{
    let a = setTimeout(()=>{setAlert(false)}, 2000)
    // useEffect 동작 전에 실행
    return ()=>{
      clearTimeout(a)
    }
    console.log(1)
  }, [])
  
  return(
    <div className="container">
      {/* {
        alert==true
        ? <div className="alert alert-warning">
          2초 이내 구매 시 할인
        </div>
        : null
      } */}
      
      {count}
      <button onClick={()=>setCount(count+1)}>버튼</button>
      <div className="row">
        <div className="col-md-6"d>
          <img src={`https://codingapple1.github.io/shop/shoes${id}.jpg`} width="100%" />
        </div>
        <div className="col-md-6">
          <h4 className="pt-5">{shoe.title}</h4>
          <p>{props.shoes[id].content}</p>
          <p>{props.shoes[id].price}원</p>
          <button className="btn btn-danger" onClick={()=>{dispatch((addItem(shoe)))}}>주문하기</button> 
        </div>
      </div>

      <Nav variant="tabs" defaultActiveKey="link0">
        <Nav.Item>
          <Nav.Link eventKey="link0" onClick={()=>{setTab(0)}} >버튼0</Nav.Link>
        </Nav.Item>
        <Nav.Item>
          <Nav.Link eventKey="link1" onClick={()=>{setTab(1)}}>버튼 1</Nav.Link>
        </Nav.Item>
        <Nav.Item>
          <Nav.Link eventKey="link2" onClick={()=>{setTab(2)}}>버튼 2</Nav.Link>
        </Nav.Item>
      </Nav>

      <TabContent tab={tab} shoes={props.shoes}/>

    </div> 
  );
};

function TabContent({tab, shoes}) {

  let {stock} = useContext(Context1);
  
  return (
  <div className="start end">
    {[<div>{stock[0]}</div>,<div>내용1</div>,<div>내용2</div>][tab]}
  </div> 
  )
  // if (props.tab==0) {
  //   return <div>내용0</div>
  // } else if (props.tab==1) {
  //   return <div>내용1</div>
  // } else if (props.tab==2) {
  //   return <div>내용2</div>
  // }
}

export default Detail;