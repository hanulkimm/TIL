# Local Storage
## 상태 유지하기
- 현재 앱을 재실행 하거나 새로 고침을 하면 초기 값으로 돌아감
## Window.localStorage
- 브라우저의 내장 객체 중 하나
- key-value 형태로 데이터를 저장할 수 있는 저장소
- localStorage에 저장된 데이터는 브라우저를 종료해도 계속해서 유지 됨
- 단, 보안과 관련된 중요한 정보를 저장하기에는 적합하지 않음
### `localStorage.setItem(key, value)`
- key,value 형태로 데이터 저장
- 데이터 저장 시 문자열 형태로 저장됨

![image](https://user-images.githubusercontent.com/122726684/236717548-5b269827-e585-4c9e-821b-cca7b11b5a06.png)

### `localStorage.getItem(key)`
- key값으로 저장된 데이터 불러오기
- 데이터 저장 시, 문자열 형태로 저장되므로 불러올때도 문자열로 불러옴

![image](https://user-images.githubusercontent.com/122726684/236717623-bab68828-67d7-4683-a0ab-7ba7c20d6a61.png)

### `JSON.stringify`
- JSON(JavaScript Object Notation) 객체의 메서드
- 자바스크립트 객체를 JSON 형식의 문자열로 변환하여 반환

![image](https://user-images.githubusercontent.com/122726684/236717801-08dd4ba1-19f5-4952-bb43-c0793bbd23e6.png)

### `JSON.parse`
- JSON 형식의 문자열을 자바스크립트 객체로 변환하여 반환

![image](https://user-images.githubusercontent.com/122726684/236717876-d857b37c-9bdb-460c-92ba-54a55776450c.png)

### 실습
![image](https://user-images.githubusercontent.com/122726684/236728598-d4ee10e7-b2a3-493b-b892-68f6b29a708b.png)

# plugins
- vuex store에 추가적인 기능을 제공하는 확장 기능
- state의 변화를 감지해, 애플리케이션 성능 최적화의 목적을 가짐

## vuex-persistedstate
- vuex state의 상태를 브라우저 local storage에 저정해주는 plugin
- 페이지를 새로 고침하거나 브라우저를 종료하였다가 다시 열었을 때, 이전 상태를 유지할 수 있도록 해줌

### 실습
- 설치 : `$npm i vuex-persistedstate`
- 적용

![image](https://user-images.githubusercontent.com/122726684/236718163-45181f26-2721-4692-a71d-92d8170d3519.png)

# Vuex Binding Helper
- vuex store의 state, mutations, actions 등을 간단하게 사용할 수 있도록 만들어진 헬퍼 함수
- mapState, mapActions와 같은 형식으로 사용
- 사용하기 위해서는 import 받아와야 함
- `import { mapState, mapActions} from 'vuex'`

## mapState
- vuex store의 상태를 컴포넌트의 데이터에 매핑할 떄 사용
- 객체 혹은 배열 형태로 상태를 매핑하여 사용할 수 있음
### 객체 형태로 매핑
1. mapState를 import
2. spread operator를 사용하여 mapState를 전개
3. mapState 내부에 불러오고자 하는 값을 정의
- 화살표 함수를 사용
- key값은 다른 이름으로 변경하여 사용할 수 있음

![image](https://user-images.githubusercontent.com/122726684/236726041-0a1dced0-b3de-4d2b-bd06-c7491818a58d.png)

### 배열 형태로 매핑
1. mapState를 import
2. spread operator를 사용하여 mapState를 전개
3. vuex store의 상태 중, 불러오고자 하는 대상을 배열의 원소로 정의

![image](https://user-images.githubusercontent.com/122726684/236726131-c3afeef2-736f-4da3-944d-b3459a7a4838.png)

## mapActions
- 컴포넌트에서 `this.$store.dispatch()`를 호출하는 대신, 액션 메서드를 직접 호출하여 사용할 수 있음

### 배열 형태로 매핑
![image](https://user-images.githubusercontent.com/122726684/236727201-4b01ed0e-9a05-477c-853c-6a1fa966f082.png)
### 객체 형태로 매핑
![image](https://user-images.githubusercontent.com/122726684/236727246-3aac1085-6a1a-4e47-be3d-073a4171898e.png)

## mapGetters
![image](https://user-images.githubusercontent.com/122726684/236727291-13fda02b-26e3-4c61-b346-47e3b77d7af9.png)
- 상황에 따라서는 배열, 객체 형태로 각각 매핑하여 사용 할 수 있음

![image](https://user-images.githubusercontent.com/122726684/236727318-53c72f7e-daa5-4147-9915-20610cf41b04.png)

# Modules
- vuex store를 여러 파일로 나눠서 관리 할 수 있게 해 주는 기능
- vuex store와 동일한 구성을 가진 별도의 객체를 정의하여 modules 옵션에 작성한 객체를 추가하여 사용
- 별개의 .js 파일에 정의하고 import하는 방식으로도 사용 가능
- store의 가독성을 향상시킬 수 있음

![image](https://user-images.githubusercontent.com/122726684/236728438-f68f5d93-4281-4429-843e-fd8244fb073a.png)

![image](https://user-images.githubusercontent.com/122726684/236728464-3386c6c4-4d10-466a-a880-6b6b684c2cfa.png)