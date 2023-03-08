# CSS

## Box Model
- 모든 HTML 요소는 박스로 이루어짐
- 하나의 박스는 네 부분(영역)으로 이루어짐
  - Content: 글이나 이미지 등 요소의 실제 내용
  - Padding: 테두리 안쪽의 내부 여백, 요소에 적용된 배경색, 이미지까지 적용
  - Border: 테두리 영역
  - Margin: 테두리 바깥의 외부 여백, 배경색을 지정할 수 없다
```css
.margin{
  margin: 10px; # 상하좌우
  margin: 10px 20px; # 상하/좌우
  margin: 10px 20px 30px; # 상/좌우/하
}
.border{
  border: 2px dashed black; # width, style, color
}
```
### Box-sizing
- 기본적으로 모든 요소의 box-sizing은 content-box
  - padding 제외한 순수 content영역만을 box로 지정
- border까지의 너비를 100px으로 보기 위해서 box-sizing을 border-box로 지정


## CSS Display
### display: block
- 줄 바꿈이 일어나는 요소
- 화면 크기 전체 가로 폭을 차지
  - 너비 설정하면 설정 안 한 만큼은 margin으로 자동 부여
- 블록 요소 안에 인라인 요소가 들어갈 수 있음
- 대표적인 블록 레벨 요소: div / ul,ol,il / p / hr / form
### display: inline
- 줄 바꿈이 일어나지 않는 행의 일부 요소
- content를 마크업하고 있는 만큼만 가로 폭 차지
- width, height, margin-top, margin-bottom 지정할 수 없음
- 상하여백은 line-height로 지정
- text-align: center/ left/ right 통해 수평 정렬
- 대표적인 인라인 레벨 요소: span/ a/ img/ input, label
### display: inline-block
- block과 inline 요소의 특징을 모두 가짐
### display: none
- 해당 요소를 화면에 표시하지 않고 공간조차 부여하지 않음
- visibility: hidden은 해당 요소가 공간을 차지하나 화면에 표시만 하지 않는다.

## CSS position
- 문서 상에서 요소의 위치를 지정(어떤 기준으로 어디에 배치)
- static, relative, absolute, fixed, sticky
### Static
- 모든 태그의 기본 값
- 일반적인 요소의 배치 순서에 따름
- 부모 요소 내에서 배치될 때는 부모 요소의 취를 기준으로 배치 됨
### Relative 상대 위치
- 자기 자신의 static위치를 기준으로 이동
- normal flow 유지
- 레이아웃에서 요소가 차지하는 공간은 static일 때와 같음
### Absolute 절대 위치
- normal flow에서 벗어남(레이아웃에 공간 차지하지 않음)
- static이 아닌 가장 가까이 있는 부모/조상 요소를 기준으로 이동(없는 경우 body)
### Fixed 고정 위치
- normal flow에서 벗어남(레이아웃에 공간 차지하지 않음)
- 부모 요소와 관계없이 viewport를 기준으로 이동(스크롤시에도)
### Sticky 
- 스크롤에 따라 static에서 fixed로 변경

## CSS 원칙
1. Normal Flow
- 모든 요소는 네모(박스 모델), 좌측 상단에 배치
- display에 따라 크기와 배치가 달라짐

2. Position
- position으로 위치의 기준을 변경
  - relative: 본인의 원래 위치
  - absolute: 특정 부모의 위치
  - fixed: 화면의 위치