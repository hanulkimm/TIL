import {Table} from 'react-bootstrap';
import { useSelector } from 'react-redux';

function Cart() {
  let info = useSelector((state)=>state.info)
  console.log(info)

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
            info.map((a)=>{
              return(
              <tr>            
                <td>#</td>
                <td>{a.name}</td>
                <td>{a.count}</td>
                <td>안녕</td>
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