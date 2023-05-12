# 관통 프로젝트_09
## Vue를 활용한 SPA 구성

### 프로젝트 목표
- 영화 정보를 제공하는 SPA 제작
- AJAX통신과 JSON 구조에 대한 이해
- Vue CLI, Vue Router 프러그인 활용

![image](https://github.com/hanulkimm/codingtestprep/assets/122726684/a5f6fc42-909d-44a7-be1a-efbdbd9c3596)

### 겪은 어려움
1. api key를 숨기는 데 어려움이 있었다. 
2. 보고 싶은 영화 리스트를 작성하는데 새로고침하면 저장되지 않는 문제가 발생했다. localStorage를 활용하는데 영화를 update할 때마다 저장을 하는데 어려움을 겪었다.
3. 보고 싶은 영화를 누르면 밑줄이 그어져야 되는데 localStorage에 업데이트가 제대로 되지 않았다.
4. random 영화를 보여주는 RandomView에서 새로고침을 하면 영화가 보여지지 않았다. 

### 해결방안
1. .env.local 파일은 가장 상위 폴더 밖의 폴더에 만들어서 생긴 오류였다. 파일을 이동 시킨 후에 서버를 다시 켰더니 api key를 제대로 불러 올 수 있었다. 
2. 우선, WatchListForm에서 form으로 입력받은 movie를 store로 넘겨주고 state에 있는 WatchList에 저장해주었다. 그런 다음에 localStorage의 데이터를 갱신시켜주기 위해 watchList 를 json 형식으로 바꿔주고 새로운 watchList로 localStorage를 바꿔주었다. 다음에 MovieView 페이지가 created 될 때 state에 있는 movies를 불러오고 movie 각각을 MovieCard vue로 넘겨주었다. 
3. state에 있는 watchList에 isActive을 같이 넘겨주었다. 만약 movie를 click했을 때 isActive 값을 반대로 바꿔주고 바꾼 watchList를 다시 localStorage에 저장해주었다. 
4. movie 데이터가 있을 때만 div 가 보여지게 하고 영화를 불러올 수 있는 button를 통해 영화를 보여주게 하였다. 