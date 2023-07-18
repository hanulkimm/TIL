import {Table} from 'react-bootstrap';
import { useDispatch, useSelector } from 'react-redux';
import { changeName } from '../store/userSlice.js';
import { changeAmount } from './../store.js';

function Cart() {
  let state = useSelector((state)=>state)
  let dispatch = useDispatch();
  console.log(state.user)

  return(
    <div>

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