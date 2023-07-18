import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import styled from 'styled-components';

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
  
  let [count, setCount] = useState(0);
  let {id} = useParams();
  let shoe = props.shoes.find((shoe)=> {
    return shoe.id==id; // ===이면 안됨!! 
  })

  let [alert, setAlert] = useState(true);
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
      {
        alert==true
        ? <div className="alert alert-warning">
          2초 이내 구매 시 할인
        </div>
        : null
      }
      
      {count}
      <button onClick={()=>setCount(count+1)}>버튼</button>
      <div className="row">
        <div className="col-md-6">
          <img src={`https://codingapple1.github.io/shop/shoes${id}.jpg`} width="100%" />
        </div>
        <div className="col-md-6">
          <h4 className="pt-5">{shoe.title}</h4>
          <p>{props.shoes[id].content}</p>
          <p>{props.shoes[id].price}원</p>
          <button className="btn btn-danger">주문하기</button> 
        </div>
      </div>
    </div> 
  );

};

export default Detail;