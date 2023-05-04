# State Management (상태 관리)
## 개념
- 상태 (State): 현재에 대한 정보(data)
- 하나의 App에 여러 component 들을 조합해서 만들어짐
- 각 component는 독립적이기 때문에 각각의 상태 가짐
- 여러 개의 component가 같은 상태(data)를 유지할 필요가 있음 --> 상태 관리(State Management)가 필요

## Centralized Store
![image](https://user-images.githubusercontent.com/122726684/236077175-dc266d78-6eb6-4412-af08-0ccdb12ca608.png)

- 중앙 저장소(store)에 데이터를 모아서 상태 관리
- 각 component는 중앙 저장소의 데이터를 사용
- component의 계층에 상관없이 중앙 저장소에 접근해서 데이터를 얻거나 변경할 수 있음
- 중앙 저장소의 데이터가 변경되면 각각의 component는 해당 데이터의 변화에 반응하여 새로 변경된 데이터를 반영함
- 규모가 크거나 컴포넌트 중첩이 깊은 프로젝트의 관리가 매우 편리

## Vuex
- 중앙 저장소를 통해 상태 관리를 할 수 있도록 하는 라이브러리
- 데이터가 예측 가능한 방식으로만 변경 될 수 있도록 하는 규칙을 설정하며, Vue의 반응성을 효율적으로 사용하는 상태 관리 기능을 제공

### 1. State
- vue instance의 data에 해당
- 중앙에서 관리하는 모든 상태 정보
- 개별 component는 state에서 데이터를 가져와서 사용
  - 개별 component가 관리하던 data를 중앙 저장소에서 관리하게 됨
- `$store.state`로 state 데이터 접근

### 2. Mutations
- 실제로 state를 변경하는 유일한 방법
- vue 인스턴스의 methods에 해당하지만 Mutatioons에서 호출되는 핸들러 함수는 반드시 동기적이어야 함
- 첫번째 인자로 state를 받으며 component 혹은 Actions에서 commit() 메서드로 호출됨

### 3. Actions
- mutations와 비슷하지만 비동기 작업을 포함할 수 있다는 차이
- state를 직접 변경하지 않고 commit()메서드로 mutations를 호출해서 state를 변경함
- context 객체를 인자로 받으며, 이 객체를 통해 store.js의 모든 요소와 메서드에 접근할 수 있음
- component에서 dispatch() 메서드에 의해 호출됨

![image](https://user-images.githubusercontent.com/122726684/236079949-4d545fc5-0c80-46bb-bd2c-9d09d154cb48.png)

### 4. Getters
- vue instance의 computed에 해당
- state를 활용하여 계산된 값을 얻고자 할 때 사용, 원본 데이터를 건들지 않고 계산된 값을 얻을 수 있음
- 종속된 값이 변경된 경우에만 재계산됨
- getters에서 계산된 값은 state에 영향을 미치지 않음
- getters에서 계산된 값은 state에 영향을 미치지 않음
- 첫번째 인자로 state, 두 번째 인자로 getter를 받음

## Vuex 실습
### 시작하기 전
- 객체 메서드 축약형 사용할 것

![image](https://user-images.githubusercontent.com/122726684/236121774-f0355d4e-ccc2-40e2-9bf1-e7fc36a771c1.png)

## vuex의 핵심 4가지
1. state
- 중앙에서 관리하는 모든 상태 정보
- `$store.state`로 접근 가능
- store의 state에 message 데이터 정의
- component에서 state 사용
  - `$store.state`로 바로 접근하기 보다 compumted에 정의 후 접근하는 것 권장

![image](https://user-images.githubusercontent.com/122726684/236122190-f6bc82a7-848c-4aea-ae72-ced57ca05cd0.png)

![image](https://user-images.githubusercontent.com/122726684/236122206-8d4e416d-21d0-4e56-8b22-752eae984b0a.png)

2. actions
- state를 변경할 수 있는 mutations 호출
- component에서 dispatch()에 의해 호출됨
- `dispatch(A,B)`
  - A: 호출하고자 하는 actions 함수
  - B: 넘겨주는 데이터(payload)

![image](https://user-images.githubusercontent.com/122726684/236122487-b307cdfb-b181-4d4a-91f7-c3edd71931d3.png)

- actions의 첫번째 인자는 context
  - context는 store의 전반적인 속성을 모두 가지고 있음
  - context.state와 context.getters를 통해 mutations를 호출하는 것이 모두 가능
  - actions에서 state를 직접 조작하는 것은 삼가야 함
- actions의 두번째 인자는 payload
  - 넘겨준 데이터를 받아서 사용

3. mutations
- actions에서 commit()을 통해 mutations 호출하기
- state를 변경하는 유일한 방법
- component 또는 actions()에서 commit()에 의해 호출됨
- `commit(A,B)`
  - A: 호출하고자 하는 mutations 함수
  - B: payload

![image](https://user-images.githubusercontent.com/122726684/236123317-dca4e38e-2e66-4608-9741-6eef32d6ea57.png)

- mutations 함수의 첫번째 인자는 state
- 두번째 인자는 payload

![image](https://user-images.githubusercontent.com/122726684/236123396-6ff608e9-a28b-4c42-9cf0-bc6f05fb14d7.png)

4. getters
- getters는 state를 활용한 새로운 변수
- getters 함수의 첫번째 인자는 state, 두 번째 인자는 getters

![image](https://user-images.githubusercontent.com/122726684/236123483-c84b82cc-4053-4ba2-85d5-b2bcc60347d0.png)

![image](https://user-images.githubusercontent.com/122726684/236123521-16b9d10d-d54d-4769-82e6-4044b68da1f2.png)

![image](https://user-images.githubusercontent.com/122726684/236123563-72bc879e-4eb1-4260-865c-734fab65f647.png)

