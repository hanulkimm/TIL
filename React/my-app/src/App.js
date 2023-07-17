import {useState} from 'react';
import './App.css';

function App() {

  let [titles, setTitles] = useState(['싸피','가기','싫어']);
  let [likes, setLikes] = useState([0,0,0]);
  let [modal, setModal] = useState(false);
  let [title, setTitle] = useState(0);
  let [input, setInput] = useState('');

  [1,2,3].map((num)=>{
    return '123'
  })

  return (
    <div className="App">
      <div className="black-nav">
        <div>블로그 만들기</div>
      </div>

      {
        titles.map((title, i)=>{
          return(
            <div className="list">
              <h4 onClick={()=>{setTitle(i); setModal(!modal)} }>{titles[i]}
                <span onClick={(e)=> {
                  e.stopPropagation();
                  let copy =[...likes]
                  copy[i] += 1
                  setLikes(copy)
                }}>❤ {likes[i]}</span>
                
              </h4>
              <p>7월 17일 발행</p>
              <button onClick={(e)=>{
                  e.stopPropagation();
                  let copy =[...titles]
                  copy.splice(i,1);
                  setTitles(copy)
                }}> 삭제</button>
            </div>
          )
        })
      }

      <input type="text" onChange={
        (e)=>setInput(e.target.value)}/>
      <button onClick={()=>{
        console.log(input)
        let copy = [...titles];
        copy.unshift(input);
        setTitles(copy);
      }}>
        Submit</button>

      {
        modal==true ? <Modal title={title} titles={titles} setTitles={setTitles} color={'yellow'} /> : null 
      }
      
    </div>
  );
}

function Modal(props) {
  return(
    <div className='modal' style={{background:props.color}} >
      <h4>{props.titles[props.title]}</h4>
      <p>날짜</p>
      <p>상세내용</p>
      <button onClick={()=>{
        let copy = [...props.titles]
        copy[0] = 'SSAFY'
        props.setTitles(copy)
      }}>글수정</button>
    </div>
  )
}


export default App;