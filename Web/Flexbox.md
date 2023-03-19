# CSS Flexible Box Layout

## 개념
![image](https://user-images.githubusercontent.com/122726684/226169742-0ae4d4bc-6238-47cd-836a-9c5ebb0edbae.png)

- 행과 열 형태로 아이템들을 배치하는 1차원 레이아웃 모델
### Flexbox 축: flex-direction : row
![image](https://user-images.githubusercontent.com/122726684/226169828-4e3e59c7-06a1-4abb-a6bd-da95d0dade1d.png)
### Flexbox 구성 요소
- Flex Container(부모 요소): 
  - flexbox 레이아웃을 형성하는 가장 기본적인 모델 
  - flex item들이 놓여있는 영역
  - display 속성을 flex 지정
- Flex Item(자식 요소)
  - 컨테이너에 속해 있는 컨텐츠(박스)
```css
.flex-container {
  display: flex;
}
/* 컨테이너 안의 아이템들은 내용물의 width를 갖고 아이템들의 height은 컨테이너와 같도록 조정됨 */
```

## Flex 속성
### 배치 설정
- flex-direction
  - main axis 기준 방향 걸정

![image](https://user-images.githubusercontent.com/122726684/226170206-d7009c54-4db1-4e98-8659-90a3f17dfab3.png)
- flex-wrap
  - 요소들이 강제로 한 줄에 배치 되게 할 것인지 여부 설정
  - wrap(넘치면 다음 줄로 배치), nowrap(기본값, 한 줄에 배치)

![image](https://user-images.githubusercontent.com/122726684/226170244-46a559a0-2fce-446f-b9e1-ab84419a22fc.png)

- flex-flow
  - flex-direction 과 flex-wrap에 대한 설정 값을 차례로 작성
  - 예시 : `flex-flow : row nowrap;`

### 공간 나누기
- justify-content
  - main axis를 기준으로 공간 배분


![image](https://user-images.githubusercontent.com/122726684/226170359-daed821a-5907-4893-8a8b-2d943a8b6b65.png)

- align-content
  - cross axis를 기준으로 공간 배분
  - 아이템이 한 줄로 배치되는 경우 확인할 수 없음

![image](https://user-images.githubusercontent.com/122726684/226170409-75cd8ed8-e5dd-40d4-b724-8b6b28bebe91.png)

- 공간 배분
  - flex-start(기본값): 아이템들을 axis 시작점으로
  - flex-end: 아이템들을 axis 끝 쪽으로
  - center : 아이템들을 axis 중앙으로
  - space-between: 아이템 사이의 간격을 균일하게 분배
  - space-around: 아이템을 둘러싼 영역을 균일하게 분배(가질 수 있는 영역을 반으로 나눠서 양쪽에)
  - space-evenly : 전체 영역에서 아이템 각 간격을 균일하게 분배

### 정렬
- align-items
  - 모든 아이템들을 cross axis 기준으로

![image](https://user-images.githubusercontent.com/122726684/226170595-190cc7b1-5c00-44a4-9cda-3eb19e6d52ea.png)
- align-self(개별 아이템)

![image](https://user-images.githubusercontent.com/122726684/226170635-28eb2d09-98f3-433d-b2ab-79481595398c.png)

- 속성
  - strech(기본값): 컨테이너 가득 채움
  - flex-start : 위
  - flex-end : 아래
  - center : 가운데
  - baseline: 텍스트 baseline에 기준선을 맞춤


### 기타 속성
- flex-grow: 남은 영역을 아이템에 분배
- order: 배치 순서
![image](https://user-images.githubusercontent.com/122726684/226171093-bc78e851-c602-4363-a415-9981302a0d41.png)

### 활용
- 수직, 수평 가운데 정렬

![image](https://user-images.githubusercontent.com/122726684/226171116-2e0ad138-af81-4a10-b538-30383d1db965.png)

- 카드 배치

![image](https://user-images.githubusercontent.com/122726684/226171170-38dabe51-33b0-45e9-88a9-381ac1f7ada2.png)