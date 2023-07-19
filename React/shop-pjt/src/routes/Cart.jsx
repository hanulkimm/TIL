import {Table} from 'react-bootstrap';
import { useDispatch, useSelector } from 'react-redux';
import { changeName } from '../store/userSlice.js';
import { changeAmount } from './../store.js';
import { useState, memo } from 'react';

let Child = memo(
  function(){
  return <div>자식임</div>
})

function Cart() {
  let state = useSelector((state)=>state)
  let dispatch = useDispatch();
  console.log(state.user)
  let [count, setCount] = useState(0);
  

  return(
    <div>
      <Child></Child>
      <button onClick={()=>{setCount(count+1)}}>+</button>
      <Table>
        <thead>
          <tr>
            <th>#</th>
            <th>상품명</th>
            <th>수량</th>
            <th>변경하기</th>
          </tr>
        </thead>
        <tbody>
          {
            state.info.map((a,i)=>{
              return(
              <tr>            
                <td>#</td>
                <td>{a.name}</td>
                <td>{a.count}</td>
                <td>
                  <button onClick={()=>{
                    dispatch(changeAmount(i))
                    }}>+</button>
                </td>
              </tr>
              )
            })
          }
          
        </tbody>
      </Table> 
    </div>
  )
}

export default Cart;