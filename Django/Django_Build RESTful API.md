# Django REST framework - Single Model
## 사전 준비
- urls 등록
```python
# drf/urls.py
urlpatters = [
  path('admin/', admin.site.urls),
  path('api/v1/', include('articles.urls')),
]

# drf/articles/urls.py
urlpatterns = [
  path('articles/',views.article_list),
  path('articles/<int:article_pk/', views.article_detail)
]
```
- article 모델 작성 및 migration 진행
- fixtures 데이터 load
- DRF 설치, 등록 및 패키지 목록 업데이트
```python
# $ pip install djangorestframework

# settings.py
INSTALLED_APPS = [
  'rest_framework',
  ...
]
```

## ModelSerializer
- articles/serializers.py 에 ModelSerializer 작성
```python
from rest_framework import serializers
from .models import Article

class ArticleListSerializer(serializers.ModelSerializer):
  class Meta:
    model = Article
    fields = ('__all__')
```

## GET (게시글 데이터 목록 조회하기)
- DRF에서 api_view decorator 작성 필수!
```python
# articles/views.py
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Article
from .serializers import ArticleListSerializer

@api_view(['GET'])
def article_list(request):
  articles = Article.objects.all()
  serializer = ArticleListSerializer(articles, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def article_detail(request,article_pk):
  article = Article.objects.get(pk=article_pk)
  serializer = ArticleListSerializer(article)
  return Response(serializer.data)
```

## POST (게시글 데이터 생성하기)
- 요청에 대한 데이터 생성이 성공했을 경우 201 상태 코드를 응답하고 실패 했을 경우는 400 Bad request를 응답
- `is_valid()` 유효성 검사가 있는 경우 `raise_exception` 인자를 사용할 수 있음
  - DRF에서 제공하는 기본 예외 처리기에 의해 자동으로 처리되며 기본적으로 HTTP 400 응답을 반환 
```python
from rest_framework import status

@api_view(['GET','POST'])
def article_list(request):
  if request.method=="GET":
    articles = Article.objects.all()
    serializer = ArticleListSerializer(articles, many=True)
    return Response(serializer.data)
  elif request.method=="POST":
    serializer = ArticleListSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
```

## DELETE (게시글 데이터 삭제하기)
- 요청에 대한 데이터 삭제가 성공했을 경우는 204 No Content 상태 코드 응답
```python
from rest_framework import status

@api_list(['GET','DELETE'])
def article_detail(request,article_pk):
  article = Article.objects.get(pk=article_pk)
  if request.method=='GET':
    serializer = ArticleListSerializer(article)
    return Response(serializer.data)
  elif request.method=='DELETE':
    article.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
```

## PUT (게시글 데이터 수정하기)
- 요청에 대한 데이터 수정이 성공했을 경우 200 OK 상태 코드 응답
```python
from rest_framework import status

@api_list(['GET','DELETE','PUT'])
def article_detail(request,article_pk):
  article = Article.objects.get(pk=article_pk)
  if request.method=='GET':
    serializer = ArticleListSerializer(article)
    return Response(serializer.data)
  elif request.method=='DELETE':
    article.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  elif request.method=='PUT':
    serializer = ArticleListSerializer(article, data=request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      return Reponse(serializer.data)
```

# Django REST framework - N:1 Relation
## 사전 준비
- Comment 모델 작성 및 DB 초기화
- Migration 진행
- fixtures 데이터 load
- CommentSerializer 및 urls 작성
```python
# urls
urlpatterns = [
  path('comments/', views.comment_list),
]

# articles/serializers.py
from .models import Comment
class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = '__all__'
```
## GET (댓글 데이터 목록 조회하기)
```python
# articles/views.py
from .models import Article, Comment
from .serializers import ArticleListSerializer, CommentSerializer

@api_view(['GET'])
def comment_list(request):
  comments = Comment.objects.all()
  serializer = CommentSerializer(comments, many=True)
  return Response(serializer.data)
```

## GET (단일 데이터 조회하기)
```python
urlpatterns = [
  path('comments/<int:comment_pk>/', views.comment_detail),
]

# articles/views.py
@api_view(['GET'])
def comment_detail(request, comment_pk):
  comment = Comment.objects.get(pk=comment_pk)
  serializer = CommentSerializer(comment)
  return Responce(serializer.data)
```

## POST (단일 댓글 생성하기)
- Comment 생성 시 유효성 검사 할 때 article field가 채워져 있지 않아 오류가 뜨기 때문에 이를 읽기 전용 필드로 설정함
  - 읽기 전용 필드는 데이터를 전송하는 시점에 '해당 필드를 유효성 검사에서 제외시키고 데이터 조회 시에는 출력'하도록 함
```python
# articles/urls.py
urlpatterns = [
  path('articles/<int:article_pk>/comments/', views.comment_create),
]

# articles/views.py
@api_view(['POST'])
def comment_create(request, article_pk):
  article = Article.objects.get(pk=article_pk)
  serializer = CommentSerializer(data=request.data)
  if serializer.is_valid(raise_exception=True): # article field가 오류 걸림(읽기 전용 필드 설정)
    serializer.save(article=article)
    return Reponse(serializer.data, status)

# articles/serializers.py
class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment
    field = '__all__'
    read_only_fields = ('article',)
```

## DELETE & PUT (댓글 데이터 삭제/수정하기)
```python
@api_view(['GET','DELETE','PUT'])
def comment_detail(request, comment_pk):
  comment = Comment.objects.get(pk=comment_pk)
  if request.method=="GET":
    serializer = CommentSerializer(comment)
    return Response(serializer.data)
  elif request.method=="DELETE":
    comment.delete()
    return Response(status = status.HTTP_204_NO_CONTENT)
  elif request.method=="PUT":
    serializer = CommentSerializer(comment, data=request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      return Response(serializer.data)
```

# N:1 역참조 데이터 조회
## 특정 게시글에 작성된 댓글 목록 출력하기
- 기존 필드 override
1. `PrimaryKeyRelatedField()`
```python
# articles/serializers.py
class ArticleSerializer(serializers.Modelserializer):
  comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
  class Meta:
    model = Article
    fields = '__all__'
```
2. Nested relationships
```python
# articles/serializers.py
class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Article
    fields = '__all__'
    read_only_fields = ('article',)

class ArticleSerializer(serializers.Modelserializer):
  comment_set = CommentSerializer(many=True, read_only=True)
  class Meta:
    model = Article
    fields = '__all__'
```

## 특정 게시글에 작성된 댓글의 개수 출력하기
- 새로운 필드 추가 
- source : 필드를 채우는 데 사용할 속성의 이름, 점 표기법을 사용하여 속성을 탐색 할 수 있음
```python
# articles/serializers.py
class ArticleSerializer(serializers.Modelserializer):
  comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
  comment_count = serializers.IntegerField(source='comment_set.count',read_only=True)
  class Meta:
    model = Article
    fields = '__all__'
```

# Django shortcuts functions
## get_object_or_404
- 모델 manager objects에서 get()을 호출하지만, 해당 객체가 없을 땐 기존 DoesNotExist 에외 HTtp40를 raise 함
```python
# articles/views.py

from django.shortcuts import get_object_or_404

article = get_object_or_404(Article, pk=article_pk)
comment = get_object_or_404(Comment, pk=comment_pk)
```
## get_list_or_404
```python
# articles/views.py

from django.shortcuts import get_object_or_404

articles = get_list_or_404(Article)
comment = get_list_or_404(Comment)
```

## Serializer 활용하기
### 댓글 목록 없애고 특정 Article에서의 모든 댓글을 내려주는 API로 수정하기
```python
# articles/views.py

@api_view(['GET','POST'])
def comment_list(request, article_pk):
  article = get_objects_or_404(Article, pk=article_pk)

  if request.method=='GET':
    comments = article.comment_set.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

  if request.method=='POST':
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save(article=article)
      return Response(serializer.data)
```
### comment_set 대신 comment로, 댓글 조회 시 article id 삭제
class CommentSerializer(serializers.ModelSerializer):
  