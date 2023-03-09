# CSS Flexible Box Layout

## 개념
- 행과 열 형태로 아이템들을 배치하는 1차원 레이아웃 모델
- 축: main axis, cross axis
- 구성 요소
  - Flex Container: flext item들이 놓여있는 영역, display 속성을 flex로 지정
  - Flex Item: 컨테이너에 속해 있는 컨텐츠

## Flex 속성
### 배치 설정
- flex-direction: main axis 기준 방향 걸정
  - row, row-reverse, column, column-reverse
- flex-wrap: 요소들이 강제로 한 줄에 배치 되게 할 것인지 여부 설정
  - wrap(넘치면 다음 줄로 배치), nowrap(기본값, 한 줄에 배치)

### 공간 나누기
- justify-content(main axis를 기준으로 공간 배분)
  - flex-start, flex-end, center, space-between, space-around, space-evenly
- align-content(cross axis를 기준으로 공간 배분)
  - flex-start, flex-end, center, space-between, space-around, space-evenly
### 정렬
- align-items(모든 아이템들을 cross axis 기준으로)
  - stretch(컨테이너를 가득 채움), flex-start, flex-end, center, baseline
- align-self(개별 아이템)
