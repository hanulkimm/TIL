# HTML
## 기본 구조
- html: 문서의 최상위(root) 요소
- head : 문서 메타데이터 요소
  - 문서 제목, 인코딩, 스타일, 브라우저에 나타나지 않는 내용
- body: 문서 본문 요소
  - 실제 화면 구성과 관련된 내용

## 요소
`<h1>contents</h1>`
- HTML의 요소는 태그와 태그 사이에 위치한 내용으로 구성되어 있음
- 내용이 없는 태그들 : br, hr, img, input, link, meta
- 요소는 중첩될 수 있음
- 여는 태그와 닫는 태그의 쌍을 잘 확인해야함
  - 오류 반환하지 않고 레이아웃 깨진 상태로 출력함

## 속성
`<a name="value"></a>`
- name: 속성명, value: 속성값
- 예시:
  `<a href="https://google.com"></a>`
- '=' 공백 없이, 쌍따옴표 사용
- 속성을 통해 태그의 부가적인 정보 설정할 수 있음
- 요소는 속성을 가질 수 있으며 속성은 요소의 시작 태그에 작성
- 태그 상관없이 사용 가능한 속성들도 있음
### HTML Global Attribute
- 모든 HTML요소가 공통으로 사용할 수 있는 속성
  - id: 문서 전체에서 유일한 고유 식별자 지정
  - class: 공백으로 구분된 해당 요소의 클래스 목록
  - style: inline 스타일

## HTML 문서 구조화

### 텍스트 요소
- `<a></a>` : href 속성을 활용하여 다른 url로 연결하는 하이퍼링크 생성
- `<b></b>`, `<strong></strong>`: 굵은 글씨 요소
- `<br>` : 텍스트 내에 줄 바꿈 생성
- 등등...
### 그룹 컨텐츠
- `<p></p>`: 하나의 문단(paragraph)
- `<div></div>`: 의미 없는 블록 레벨 컨테이너
- `<hr>`: 주제 분리하기 위한 수평선

### Input label
- label을 클릭하여 input자체에 초점을 맞추거나 활성화 시킬 수 있음
-  `<input>`에 id 속성을 `<label>`에 for 속성이 일치해야함!!!
```html
<label for="argreement">개인정보 수집에 동의합니다.</label>
<input type="checkbox" name="agreement" id="agreement">
```
### Input 유형
- 일반
  - text: 일반 텍스트 입력
  - password: 입력 시 값이 보이지 않고 문자를 특수기호로 표현
  - email: 이메일 형식이 아닌 경우 제출 불가
  - file: accept 속성을 활용하여 파일 타입 지정 가능
- 항목 중 선택
  - checkbox: 다중 선택
  - radio: 단일 선택

# CSS

## CSS
- CSS구문은 선택자를 통해 스타일을 지정할 HMTL 요소를 선택
- 중괄호 안에서는 속성과 값, 하나의 쌍을 이루어진 선언을 진행
- 예시  
`<h1 style="color:blue; font-size: 100px;">Hello<h/1>`  
- 예시2
```html
<head>
  h1 {
    color: blue;
    font-dize: 100px;
  }
</head>
```
## CSS 정의 방법 
- 인라인(inline): 해당 태그에 직접 style 속성을 활용
- 내부 참조(embedding): `<head>` 태그 내에 `<style>`에 지정
- 외부 참조(link file): 외부 CSS 파일을 `<head>`내 `<link>`를 통해 불러오기
  
### CSS 선택자 
- 기본 선택자: 
  - 전체 선택자(*)
  - 요소 선택자(tag)
  - 클래스 선택자(class): 마침표(.)문자로 시작
  - 아이디 선택자(id): # 문자로 시작
  - 속성 선택자(attr)
- 결합자(Combinators): 자손 결합자, 자식 결합자
  
- 우선순위: 인라인 > id > class, 속성 > 요소
  