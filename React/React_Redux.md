## Redux

### 설치
```
npm install @redux/toolkit react-redux
```
- 단, react와 react-dom의 버전은 18.1 이상이어야 됨

### 셋팅
```js
// store.js
import {configureStore, createSlice} from '@reduxjs/toolkit'

// user state 생성
let user = createSlice({
  name: 'user',
  initialState: 'kim',
}) 

export default configureStore({
  reducer:{
    user:user.reducer
  }
})

// index.js
import { Provider } from "react-redux";
import store from './store.js'

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <Provider store={store}>
      <BrowserRouter>
        <App />
      </BrowserRouter>
    </Provider>
  </React.StrictMode>
); 

// Cart.js
// redux store에 있는 state 사용하기
import { useSelector } from "react-redux"

function Cart(){
  let a = useSelector((state) => { return state } )
  let user = useSelector((state)=>state.user)
  console.log(a)

  return (생략)
}
```

## store의 state 변경
### 간단한 state 변경
1. state 수정해주는 함수 생성
2. 함수 export 해주기
3. import 해서 사용할 때 dispatch()로 감싸서 사용하기
```js
// store.js
let user = createSlice({
  name: 'user',
  initialState: 'kim',
  reducers :{
    changeName(state){
      return 'john' + state
    }
  }
}) 

export let {changeName} = user.actions

// cart.js
function Cart() {
  let state = useSelector((state)=>state)
  let dispatch = useDispatch();

  <button onClick={()=>{
    dispatch(changeName())
    }}>+</button>
}
```
### state가 array/object인 경우
1. state가 object인 경우
- 파라미터 받아서 사용가능 (action.payload)
```js
// store/userSlice.js

import { createSlice } from "@reduxjs/toolkit";

let user = createSlice({
  name: 'user',
  initialState: {name: 'kim', age: 20},
  reducers :{
    changeName(state, action){
      state.age += action.payload
    }
  }
  
});

export let {changeName} = user.actions

export default user;
```
2. state가 array인 경우
```js
// store.js
let info = createSlice({
  name: 'info',
  initialState: [
    {id : 0, name : 'White and Black', count : 2},
    {id : 2, name : 'Grey Yordan', count : 1}
  ],
  reducers:{
    changeAmount(state, i) {
      state[i.payload].count += 1 
    },
    addItem(state, action){
      state.push(action.payload)
    }
  }
});

export let {changeAmount, addItem} = info.actions

// cart.js
<button onClick={()=>{
  dispatch(changeAmount(i))
  }}>+</button>
```