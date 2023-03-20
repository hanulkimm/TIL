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
from .models import Article
# articles/views.py
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
  return render(request, 'articles/new.html')

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