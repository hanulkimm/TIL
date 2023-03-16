# Django URLs

## Variable routing
- URL 주소를 변수로 사용하는 것을 의미
- URL 일부를 변수로 지정하여 view 함수의 인자로 넘길 수 있음
- 변수 값에 따라 하나의 path()에 여러 페이지를 연결 시킬 수 있음
## 작성하기
- 변수는 '<>'에 정의하며 view 함수의 인자로 할당됨
- 기본 타입은 string
## 예시
```python
# urls.py
urlpatterns = [
  path('hello/<str:name>/', views.hello)
]
# articles/views.py
def hello(request, name):
  context = {
    'name' : name,
  }
  return render(request, 'hello.html', context)
```

## App URL mapping
- 앱이 많아졌을 때 urls.py를 각 app에 매핑하는 방법 
- 하나의 프로젝트에 여러 앱이 존재한다면, 각각의 앱 안에 urls.py를 만들고 프로젝트 urls.py에서 각 앱의 urls.py파일로 URL 매핑을 위탁할 수 있음
- 각각의 app 폴더 안에 urls.py를 작성

### Including other URLconfs
- include(): 다른 URLconf(app/urls.py)들을 참조할 수 있도록 돕는 함수
- include 되는 앱의 url.py에 urlpattaerns가 빈 리스트라도 작성되어야 함
```python
from django.urls import path, include
urlpatterns = [
  path('articles', include('articles.urls'))
  path('pages', include('pages.urls'))
]
```

## Naming URL patterns
- 링크에 직접 url을 작성하는 것이 아니라 path() 함수의 name 인자를 정의해서 사용
- DTL tag중 하나의 url 태그를 사용해서 path() 함수에 작성한 name을 사용할 수 있음
- URL 설정에 정의된 특정한 경로들의 의존성을 제거할 수 있음
```python 
# articles/urls.py
urlpatterns = [
  path('index/', views.index, name='index')
  path('greeting/', views.index, name='greeting')
  path('dinner/', views.index, name='dinner')
]
```
```
# index.html
{% block content %}
  <a href="{% url 'articles:dinner' %}>dinner바로가기</a>

```