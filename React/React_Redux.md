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
import { useSelector } from "react-redux"

function Cart(){
  let a = useSelector((state) => { return state } )
  let user = useSelector((state)=>state.user)
  console.log(a)

  return (생략)
}
```

## store의 state 변경
