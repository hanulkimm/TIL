# Django Template
- 데이터 표현 제어하는 도구이자 표현과 관련된 로직
- Django Template 이용한 HTML 정적 부분과 동적 컨텐츠 삽입

## Django Template Langauge
### Variable `{{ variable }}`
- 변수명은 영어, 숫자, 밑줄(_)의 조합으로 구성될 수 있음
- dot(.)를 사용하여 변수 속성에 접근 가능
- render()의 세번째 인자로 {'key':value}와 같은 딕셔너리 형태로 넘겨주며, key에 해당하는 문자열이 template에서 사용 가능한 변수명이 됨

### Filters `{{ variable|filter }}`
- 표시할 변수를 수정할 때 사용
- 60개의 built-in template filter 제공 (공식 문서 참고하기)
- 예시:
```html
{{ name|lower }}
```

### Tags `{% tag %}`
-출력 텍스트를 만들거나 반복 또는 논리를 수행하여 제어 흐름을 만드는 등 변수보다 복잡한 일들을 수행
- 일부 태그는 시작과 종료 태그 필요 `{% if  }  {% endif %}`
- 약 24개의 built-in template tags 제공

### Comments 
- 한 줄: `{# #}` 
- 여러 줄: `{% comment %} {% endcomment %}`

## Template inheritance
- 템플릿 상속은 코드의 재사용성에 초점을 맞춤
- 템플릿 상속을 사용하면 사이트의 모든 공통 요소를 포함하고 하위 템플릿이 재정의 할 수 있는 블록을 정의하는 기본 'skeletion' 템플릿을 만들 수 있음

### 템플릿 상속에 관련된 태그
- 블록: `{% block content %}{% endblock content %}`
  - 하위 템플릿에서 재정의(override)할 수 있는 블록을 정의
  - 하위 템플릿이 채울 공감
  - 가독성을 높이기 위해 선택적으로 endblock 태그에 이름을 지정할 수 있음
- 확장 : `{% extends '' %}`
  - 자식(하위) 템플릿이 부모 템플릿을 확장한다는 것을 알림
  - !!주의!! 반드시 템플릿 최상단에 작성되어야 함 (2개 이상 사용 불가) 
### Base.html
- 모든 앱에서 상속 받기 위해서 base.html을 프로젝트 상단에 두기! 
- settings의 Templates에사 `DIRS : [BASE_DIR / 'templates']` 작성
### 사용 순서
1. pjt 폴더에 template 폴더를 만들고 base.html 파일 생성  
2. base 파일에 skeleton 템플릿 작성, '<body>' 안에 {% block content %}{% endblock content %}` 사용
3. 다른 폴더 속의 하위 템플릿에서 base template 상속 받음
```
{% extends 'base.html' %}
{% block content %}
  보일 내용
{% endblock content %}

```
