# Vue with DRF
## Server & Client
### 서버 (Server)
- 클라이엔트에게 정보와 서비스를 제공하는 컴퓨터 시스템
- 서비스 전체를 제공 --> Django Web Service
  - Django를 통해 전달받은 HTML에는 하나의 웹 페이지를 구성할 수 있는 모든 데이터가 포함
  - 서버에서 모든 내용을 렌더링하여 하나의 HTML 파일로 제공
  - 정보를 포함한 web 서비스를 구성하는 모든 내용을 서버 측에서 제공
- 정보를 제공 --> DRF API Service
  - Django를 통해 관리하는 정보만을 클라이언트에게 제공
  - DRF를 사용하여 JSON으로 변환

### 클라이언트 (Client)
- 서버가 제공하는 서비스에 적잘한 요청을 통해 서버로부터 반환 받은 응답을 사용자에게 표현하는 기능을 가진 프로그램 혹은 시스템
- 서버가 제공하는 서비스에 적절한 요청
  - 서버가 정의한 방식대로 요청 인자를 넘겨 요청
  - 서버는 정상적인 요청에 적합한 응답 제공

## 정리
- Server는 정보와 서비스를 제공
  - DB와 통신하며 데이터를 생성, 조회, 수정, 삭제를 담당
  - 요청을 보낸 Client에게 정상적인 요청이었다면 처리한 결과를 응답
- Client는 사용자의 정보 요청을 처리, server에게 응답 받은 정보를 표현
  - 서버에게 정보(데이터)를 요청
  - 응답 받은 정보를 가공하여 화면에 표현


# DRF with Vue
## 실습해보기
![image](https://github.com/hanulkimm/codingtestprep/assets/122726684/6af3e1f8-d208-468e-805e-f2a3b919df8f)

## 메인 페이지 구성
- views/ArticleView.vue component 등록 및 route 등록

![image](https://github.com/hanulkimm/codingtestprep/assets/122726684/eac321ec-f545-493f-a9f7-25e14118e42d)

- App.vue에서 router link 추가

![image](https://github.com/hanulkimm/codingtestprep/assets/122726684/e50a3a2b-6a57-4126-b359-6a7f86a51791)

- ArticleView 페이지에 들어가는 ArticleList component 만들고 ArticleView에 등록하기
  
![image](https://github.com/hanulkimm/codingtestprep/assets/122726684/0970aecd-bc4d-4a2a-aa06-ec35bb806f36)

![image](https://github.com/hanulkimm/codingtestprep/assets/122726684/c7156028-823a-4515-92b8-1feef77deb1f)

- ArticleListItem component 만들고 ArticleList.vue 에 추가해주기

![image](https://github.com/hanulkimm/codingtestprep/assets/122726684/87ece175-3242-4efd-88b4-632842505806)

![image](https://github.com/hanulkimm/codingtestprep/assets/122726684/73e702f8-b458-408f-86f5-f262ac0878f2)

- store/index.js 에 articles 배열 정의
  
![image](https://github.com/hanulkimm/codingtestprep/assets/122726684/69432d83-4ee2-4409-ba4e-ae35b76dbd53)

- components/ArticleList.vue
  - state에서 articles 데이터 가져오기
  - v-for directives 활용해서 하위 컴포넌트에서 사용할 article 단일 객체 정보를 pass props

![image](https://github.com/hanulkimm/codingtestprep/assets/122726684/f323d947-a972-47bb-8e8b-1718d0bd4c28)

- components/ArticleListItem.vue
  - 내려 받은 prop 데이터로 화면 구성
  - prop 데이터 타입 정확히 명시하기

![image](https://github.com/hanulkimm/codingtestprep/assets/122726684/d060ac7d-927e-4d20-a92f-8a3e76744245)

# CORS (Cross-Origin Resource Sharing)
- 브라우저가 요청을 보내고 서버의 응답이 브라우저에 도착하는데
  - 서버는 200 정상을 반환
  - 그러나, 브라우저가 막음
- 왜? 보안상의 이유로 브라우저는 동일 출처 정책(SOP)에 의해 다른 출처의 리소스와 상호작용 하는 것을 제한 함
- 
## SOP (Same-Origin Policy)
- 동일 출처 정책
- 블러온 문서나 스크립트가 다른 출처에서 가져온 리소스와 상호작용 하는 것을 제한하는 보안 방식
- 잠재적으로 해로울 수 있는 문서를 분리함으로써 공격받을 수 경로를 줄임

### Origin 출처
- URL의 protocol, host, port를 모두 포함하여 출처라고 부름
  
![image](https://github.com/hanulkimm/codingtestprep/assets/122726684/50f58dc9-32dc-400e-aa97-e938a80bad4a)

![image](https://github.com/hanulkimm/codingtestprep/assets/122726684/f27cd830-82b3-437d-9933-441738d2f4f0)

### 교차 출처 리소스 공유
- 추가 HTTP Header를 사용하여 특정 출처에서 실행중인 웹 어플리케이션이 다른 출처의 자원에 접근할 수 있는 권한을 부여하도록 브라우저에 알려주는 체계
  - 어떤 출처에서 자신의 컨텐츠를 불러갈 수 있는지 서버에 지정할 수 있는 방법
- 리소스가 자신의 출처와 다를 때 교차 출처 HTTP 요청을 실행
  - 만약 다른 출처의 리소스를 가져오기 위해서는 이를 제공하는 서버가 브라우저에 다른 출처지만 접근해도 된다는 사실을 알려야 함
  - 교차 출처 리소스 공유 정책 (CORS policy)

### CORS 사용하기
- django-cors-headers library 사용하기

![image](https://github.com/hanulkimm/codingtestprep/assets/122726684/51dc8004-4633-4ffc-8c59-0e13e5cd2141)

- App 추가 및 MIDDLEWARE 
  - CorsMiddleware보다 CommonMiddleWare보다 먼저 정의하기!!!!!

![image](https://github.com/hanulkimm/codingtestprep/assets/122726684/ddca9980-6c95-4405-9104-5c6fd6225fd3)

- CORS_ALLOWED_ORIGINS에 교차 자원 공유를 허용할 Domain 등록

![image](https://github.com/hanulkimm/codingtestprep/assets/122726684/853e734b-50ad-4691-a984-d19f18f36741)

- 만약 모든 Origin 허용하고자 한다면,
`CORS_ALLOW_ALL_ORIGINS = True`


# Axios 사용하기
## Article Read
- axios 설치
`$ npm install axois`

- `store/index.js` 에서 getArticles 메서드 정의하기
```js
// store/index.js
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default new Vuex.Store({
  state:{
    articles:[]
  }
  mutations: {
    GET_ARTICLES(state, articles){
      state.articles = articles
    }
  },
  actions: {
    getArticles(context){
      axios({
        method:'get',
        url: `${API_URL}/api/v1/articles/`,
      })
      .then((res)=>{
        // console.log(res, context)
        context.commit('GET_ARTICLES', res.data)
      })
      .catch((err)=>[
        console.log(err)
      ])
    }
  },
  ...
})
```
- `views/ArticleView.vue` 에서 articles 호출
```vue
<script>
export default {
  name: 'ArticleView',
  components: {
    ArticleList
  },
  computed:{
  },
  created() {
    this.getArticles()
  },
  methods: {
    getArticles(){
      this.$store.dispatch('getArticles')
    }
  }
}
</script>
```
## Article Create
- router/index.js에 CreateView 추가

![image](https://github.com/hanulkimm/codingtestprep/assets/122726684/dcb1f901-4c87-4ec2-8975-d3c0d306cee2)

- 게시글 생성 위한 form 만들기

![image](https://github.com/hanulkimm/codingtestprep/assets/122726684/f0da4bdc-ecfa-46f0-97a7-e8b6d81c5bf2)

![image](https://github.com/hanulkimm/codingtestprep/assets/122726684/a39f07e2-a6a3-4d94-b743-a4f26179c1fa)

- axios 사용해 server에 게시글 생성 요청
  - state를 변화 시키는 것이 아닌 DB에 게시글 생성 후, ArticleView로 이동할 것이므로 methods에서 직접 처리

![image](https://github.com/hanulkimm/codingtestprep/assets/122726684/9104d1f2-c886-4612-97da-f747b5da9f7f)

- ArticleView에서 CreateView로 가는 router-link 생성

![image](https://github.com/hanulkimm/codingtestprep/assets/122726684/42afaf27-55c3-44a0-a854-7656c175efb3)

## Article Detail
- DetailView 만들기

![image](https://github.com/hanulkimm/codingtestprep/assets/122726684/c6a8e7e9-d7ec-4a9b-b890-57b9931f3d1a)

- router/index.에 추가해주기
  - id를 동적 인자로 입력 받아 특정 게시글에 대한 요청

![image](https://github.com/hanulkimm/codingtestprep/assets/122726684/dc9d7e26-1953-4a80-9415-590fc12ab265)

- ArticleListItem.vue에 router-link 만들기

![image](https://github.com/hanulkimm/codingtestprep/assets/122726684/afc7cbde-4b65-4ac0-bf1f-e311730b2d57)

- axios 사용해서 detail 데이터 가져오기

![image](https://github.com/hanulkimm/codingtestprep/assets/122726684/b2facacb-c79b-4d03-892b-6a6ce92f3490)

- optional chaning 활용해 데이터 표기하기

![image](https://github.com/hanulkimm/codingtestprep/assets/122726684/610ab6f7-15c9-41fa-87c3-52139f3c9477)