# Admin Site
- Django의 가장 강력한 기능 중 하나인 automatic admin interface
- 서버의 관리자가 활용하기 위한 페이지
- 모델 class를 admin.py에 등록하고 관리
- 레코드 생성 여부 확인에 매우 유용하며 직접 레코드를 삽입할 수 있음
## Admin 계정 생성
`$ python manage.py createsuperuser`
- username과 password를 입력해 관리자 계정 생성
- email은 선택사항이기 때문에 입력하지 않고 enter 입력 가능
- 비밀번호 생성 시 보안상 터미널에 입력되지 않으니 무시하고 입력 진행
## Admin에 모델 클래스 등록
- 모델의 record를 보기 우해서는 admin.py에 등록 필요
```python 
# articles/admin.py
from django.contrib import admin
from .models import Article

admin.site.register(Article)
```

# CRUD with view functions
## 사전 준비
### bootstrap CDN 및 템플릿 추가 경로 작성

![image](https://user-images.githubusercontent.com/122726684/226342816-99948a8a-5d9b-442d-816a-1a415e82cfc2.png)

###  url 분리 및 연결

![image](https://user-images.githubusercontent.com/122726684/226343031-30afb783-062e-45f3-a4dc-8aa57e41234a.png)

### index 페이지 작성
```python
# articles/urls.py
from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
  path('', views.index, name='index')
]

# articles/views.py
def index(request):
  return render(request, 'articles/index.html')
```
```html
<!-- templates/articles/index.html -->
{% extends 'base.html' %}

{% block content %}
 <h1>Articles</h1>
{% endblock content %}
```
### Article Model 작성
```python
from django.db import models

class Article(models.Model):
  title = models.CharField(max_length=10)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now=True)
```

## Read 1 (index page)
- index 페이지에서는 전체 게시글을 조회해서 출력한다
```python 
# articles/views.py
from .models import Article

def index(request):
  articles = Article.objects.all()
  context = {
    'articles' : articles,
  }
  return render(request, 'articles/index.html', context)
```
```html
<!-- templates/articles/index.html -->
{% extends 'base.html' %}

{% block content %}
 <h1>Articles</h1>
 {% for article in articles}
  <p>글 번호: {{ article.pk }}</p>
  <p>글 제목: {{ article.title }}</p>
  <p>글 내용: {{ article.content }}</p>
  {% endfor %}
{% endblock content %}
```
## Read 2 (detail page)
- 개별 게시글의 상세 페이지 제작
- 모든 게시글 마다 뷰 함수와 템플릿 파일을 만들 수는 없음
  - 글 번호(pk)를 활용하여 하나의 뷰 함수와 템플릿 파일로 대응
- variable routing 활용

### urls
- url로 특정 게시글을 조회할 수 있는 번호를 받음
### views
- Article.objects.get(pk=pk)에서 오른쪽 pk는 variable routing을 통해 받은 pk, 왼쪽 pk는 DB에 저장된 레코드의 id 컬럼
```python
# articles/urls.py
urlspatterns = [
  path('<int:pk>/', views.detail, name='detail')
]
# articles/views.py
def detail(request, pk):
  article = Article.objects.get(pk=pk)
  context = {
    'article' : article
  }
  return render(request, 'articles/dtail.html', context)
```
```html
<!-- templates/articles/detail.html -->
{% extends 'base.html' %}

{% block content %}
 <h1>Detail</h1>
 <h3>{{ article.pk }} 번째 글</h3>
 <hr>
  <p>제목: {{ article.title }}</p>
  <p>내용: {{ article.content }}</p>
  <p>작성 시각: {{ article.created_at }}</p>
  <p>수정 시각: {{ article.updated_at }}</p>
  <hr>
  <a href="{% url 'articles:index' %}">목록</a>
{% endblock content %}

<!-- templates/articles/index.html -->
<!-- 제목을 누르면 상세 페이지로 이동 -->
{% extends 'base.html' %}

{% block content %}
 <h1>Articles</h1>
 {% for article in articles}
  <p>글 번호: {{ article.pk }}</p>
  <a href="{% url 'article:detail' article.pk %}">
    <p>글 제목: {{ article.title }}</p>
  </a>
  <p>글 내용: {{ article.content }}</p>
  {% endfor %}
{% endblock content %}
```

## CREATE
- CREATE 로직 구현하기 위해서는 2개의 함수 필요
1. 사용자의 입력을 받을 페이지를 렌더링 하는 함수 1개 : "new" view function
```python
#articles/urls.py
urlpatterns = [
  path('new/', views.new, name='new'),
]
# articles/views.py
def new(request):
  return render(request, 'articles/new.html')
```
```html
<!-- templates/articles/new.html -->
{% extends 'base.html' %}

{% block content %}
 <h1>NEW</h1>
  <form action='#' method="GET">
    <label for="title">Title: </label>
    <input type="text" name="title"><br> 
    <label for="content">Content: </label>
    <textarea name="content"></textarea><br>
  <form>
  <hr>
  <a href="{% url 'articles:index' %}">뒤로</a>
{% endblock content %}
```
2. 사용자가 입력한 데이터를 전송 받아 DB에 저장하는 함수 1개: "create" view function
```python
#articles/urls.py
urlpatterns = [
  path('create/', views.new, name='create'),
]
# articles/views.py
def create(request):
  title = request.GET.get('title')
  content = request.GET.get('content')

  # 데이터 생성 3가지 방법
  # 1.
  # article = Article()
  # article.title = title
  # article.content = content
  # article save
  # 2.
  article = Article(title=title, content=content)
  article.save()
  # 3.
  # Article.objects.create(title=title, content = content)
  return redirect('articles:detail', article.pk)
```
```html
<!-- templates/articles/new.html -->
{% extends 'base.html' %}

{% block content %}
 <h1>NEW</h1>
 <form action="{% url 'articles:create' %}" method="GET">
    <label for="title">Title: </label>
    <input type="text" name="title"><br> 
    <label for="content">Content: </label>
    <textarea name="content"></textarea><br>
  <form>
  <hr>
  <a href="{% url 'articles:index' %}">뒤로</a>
{% endblock content %}
```
### 1 또는 2번째 생성 방식을 사용하는 이유
- create 메서드가 더 간단해 보이지만 추후 데이터가 저장되기 전에 유효성 검사 과정을 거치게 될 예정
- 유효성 검사가 진행된 후에 save 메서드가 호출되는 구조를 택하기 위함
### redirect
- 데이터를 가져와서 데이터베이스에 저장했고 유저는 이미 만들어져있는 url로 보내면 됨
- 인자에 작성된 곳으로 다시 요청 보냄
- 사용 가능한 인자
  - view name : `return redirect('articles:index')`
  - url : `return redirect('/articles/')`

## HTTP Method
- HTTP: 네트워크 상에서 데이터를 주고 받기 위한 약속
- HTTP Method: 데이터에 어떤 요청을 원하는지를 나타낸 것
### GET
- 어떤 데이터를 조회하는 요청
- GET 방식으로 데이터를 전달하면 Query String 형식으로 보내짐
- 특정 리소스를 가져오도록 요청 할 때 사용
- 반드시 데이터를 가져올 때만 사용해야 함
- DB에 변화를 주지 않음
- CRUD에서 R역할을 담당
### Post
- 어떤 데이터를 생성(변경)하는 요청
- POST 방식으로 데이터를 전달하면 Query String이 아닌 Body에 담겨서 보내짐
- 서버로 데이러를 전송할 때 사용
- 서버에 변경사항을 만듦
- 리소스를 생성하기 위해 데이터를 HTTP body에 담아 전송
- GET의 쿼리 스트링 파라미터와 다르게 URL로 데이터를 보내지 않음
- CRUD에서 C/U/D 역할 담당

### POST method 적용하기
- 403 Forbidden
  - 서버에 요청이 전달되었지만, 권한 때문에 거절되었다는 것 의미
  - 게시글 작성 권한이 없음 의미
  - 최소한의 신원 확인이 필요
- CSRF: Cross-Site-Request-Forgery
  - 사이트 간 요청 위조
  - 사용자가 자신의 의지와 무관하게 공격자가 의도한 행동을 하여 특정 웹 페이지를 보안에 취약하게 하거나 수정, 삭제 등의 작업을 하게 만드는 공격 방법
- CSRF 공격 방어: CSRF Token
  - 사용자의 데이터에 임의의 난수 값을 부여해 매 요청마다 해당 난수 값을 포함시켜 전송 시키도록 함
  - 이후 서버에서 요청을 받을 때 마다 전달된 token 값이 유효한지 검증
  - django는 DTL에서 csfr_token 템플릿 태그를 제공
  - `{% csrf_token %}` : 템플릿에서 내부 URL로 향하는 POST form을 사용하는 경우에 사용, 외부URL로 향하는 POST form에 대해서는 CSRF 토큰이 유출되어 취약성을 유발할 수 있기 때문에 사용해서는 안됨

```html
<!-- templates/articles/new.html -->
{% extends 'base.html' %}

{% block content %}
 <h1>NEW</h1>
 <form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    <label for="title">Title: </label>
    <input type="text" name="title"><br> 
    <label for="content">Content: </label>
    <textarea name="content"></textarea><br>
  <form>
  <hr>
  <a href="{% url 'articles:index' %}">뒤로</a>
{% endblock content %}
```
## DELETE
- 삭제하고자 하는 특정 글을 조회 후 삭제해야 함
```python
# articles/urls.py
urlpatterns = [
  path('<int:pk>/delete/', views.delete, name='delete')
]
# articles/views.py
def delete(request,pk):
  article = Article.objects.get(pk=pk)
  article.delete()
  return redirect('articles:index')
```
```html
<!-- articles/detail.html -->
{% extends 'base.html' %}

{% block content %}
  ...
  <form action="{% url 'articles:delete' article.pk %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="DELETE">
  <a href="{% url 'articles:index' %}">목록</a>
{% endblock content %}
```
## UPDATE
- 수정은 CREATE 로직과 마찬가지로 2개의 view 함수가 필요
1. 사용자의 입력을 받을 페이지를 렌더링 하는 함수 1개
  - 'edit' view function
2. 사용자가 입력한 데이터를 전송 받아 DB에 저자하는 함수 1개
  - 'update' view function
```python
# articles/urls.py
urlpatterns = [
  path('<int:pk>/edit/', views.delete, name='edit')
]
# articles/views.py
def edit(request,pk):
  article = Article.objects.get(pk=pk)
  context = {
    'article' : article, 
  }
  return render(request, 'articles/edit.html', context)
```
