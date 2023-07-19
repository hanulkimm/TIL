import { configureStore, createSlice } from "@reduxjs/toolkit";
import user from "./store/userSlice";


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

export default configureStore({
  reducer:{
    user : user.reducer,
    info: info.reducer,
  }
})