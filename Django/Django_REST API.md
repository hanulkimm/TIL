# HTTP

## HTTP 란?
- HyperText Transfer Protocol
- HTML 문서와 같은 리소스(자원)들을 가져올 수 있도록 하는 프로토콜
- 웹 상에서 컨텐츠를 전송하기 위한 약속, 모든 데이터 교환의 기초
- 클라이언트와 서버는 요청과 응답을 통해 통신

### 특징


### 대표적인 HTTP Request Methods
1. GET
- 서버에 리소스의 표현을 요청
- GET을 사용하는 요청은 데이터만 검색해야 함
2. PUSH
- 데이터를 지정된 리소스에 제출
- 서버의 상태 변경
3. PUT
- 요청한 주소의 리소스를 수정
4. DELETE
- 리소스를 삭제

### HTTP response status code
- 특정 HTTP 요청이 성공적으로 완료 되었는지 여부를 나타냄
- 5개의 그룹으로 나뉨
  - 1. Informational responpses (100-199)
  - 2. Successful responses (200-299)
  - 3. Redirection messages (300-399)
  - 4. Client error responses (400-499)
  - 5. Server error responses (500-599)

# URI
## 웹에서 리소스 식별
- HTTP 요청의 대상을 리소스(자원)이라고 함
- 리소스는 문서, 사진 또는 기타 어떤 것이든 될 수 있음
- 각 리소스는 식별을 위해 URI로 식별됨

## URI
- Uniform Resource Identifier(통합 자원 식별자)
- 인터넷에서 리소스를 식별하는 문자열
- 가장 일반적인 URI는 웹 주소로 알려진 URL
- 특정 이름 공간에서 이름으로 리소스를 식별하는 URI는 URN

## URL
- Uniform Resource Locator (통합 자원 위치)
- 웹에서 주어진 리소스의 주소
- 네트워크 상에 리소스가 어디 있는지(주소)를 알려주기 위한 약속
- URL의 구성: 


![image](https://user-images.githubusercontent.com/122726684/231614078-cd6307a8-526b-43c7-be63-4e54e9a87fdc.png)

## URL 구조
### 1. Scheme (or protocal)

![image](https://user-images.githubusercontent.com/122726684/231614504-0ecc7737-d689-4f03-bcac-28749d6f8444.png)  
- 브라우저가 리소르를 요청하는 데 사용해야 하는 프로토콜
- 브라우저가 어떤 규약을 사용하는지를 나타냄
- 기본적으로 웹은 HTTP(S)를 요구하며 메일을 열기 위한 mailto:, 파일을 전송하기 위한 ftp:등 다른 프로토콜도 존재

### 2. Authority

![image](https://user-images.githubusercontent.com/122726684/231614628-3b244c4e-f097-424f-ae79-410385465965.png)  
- Scheme 다음은 문자 패턴 ://으로 구분된 Authority(권한)이 작성됨
- domain과 port를 모두 포함하며 둘은 :(콜론)으로 구분됨
  1. Domain Name
  - 요청 중인 웹 서버
  - IP 주소를 직접 사용하는 것도 가능하지만 외우기 어렵기 때문에 도메인 이름 사용
  2. Port
  -  웹 서버의 리소스에 접근하는데 사용되는 기술적인 문(Gate)
  -  HTTP 프로토콜의 표준 포트는 HTTP-80, HTTPS-443
  -  Django의 경우 8000기 기본 포트로 설정

### 3. Path

![image](https://user-images.githubusercontent.com/122726684/231618454-614f4bed-edda-452c-86d1-bf2ea29a0b7e.png)  
- 웹 서버의 리소스 경로
- 초기에는 실제 파일이 위치한 물리적 위치를 나타냈지만 오늘날은 실제 위치가 아닌 추상화된 형태의 구조를 표현

### 4. Parameters

![image](https://user-images.githubusercontent.com/122726684/231618564-abdc8d66-ae9b-44cc-8d12-2245f1fcc1fe.png)  
- 웹 서버에 제공하는 추가적인 데이터
- 파라미터는 '&'기호로 구분되는 key-value 쌍 목록
- 서버는 리소스를 응답하기 전에 이러한 파라미터를 사용하여 추가 작업을 수행할 수 있음

### 5. Anchor

![image](https://user-images.githubusercontent.com/122726684/231618723-cfa728b6-7d7f-4295-b68d-fb65365ab962.png)  
- 리소스의 다른 부분에 대한 앵커
- 리소스 내부 일종의 북마크를 나타내며 브라우저에 해당 북마크 지점에 있는 컨텐츠를 표시
- fragment identifier라고 부는 '#' 이후 부분은 서버에 전송되지 않음
  - 브라우저에게 해당 지점으로 이동할 수 있도록 함

## URN
- Uniform Resource name (통합 자원 이름)
- URL과 달리 자원의 위치에 영향을 받지 않는 유일한 이름 역할을 함
- URL 단점 극복 위해 등장, 자원이 어디에 위치한지 여부와 관계없이 이름만으로 자원 식별
- 하지만 보편화 되어있지 않아 현재는 URL을 대부분 사용
- 예시: ISBN(국제표준 도서번호)

# REST API
## API
- Application Programming Interface
- 애플리케이션과 프로그래밍으로 소통하는 방법
  - 개발자가 복잡한 기능을 보다 쉽게 만들 수 있도록 프로그래밍 언어로 제공되는 구성
- 복잡한 코드를 추상화하여 대신 사용할 수 있는 몇 가지 더 쉬운 구문을 제공

## Web API
- 웹 서버 또는 웹 브라우저를 위한 API
- 현재 웹 개발은 여러 OPEN API를 활용하는 추세
- 다양한 타입의 데이터를 응답
  - HTML, XML, JSON 등
  
## REST
- Representational State Transfer
- API Server를 개발하기 위한 일종의 소프트웨어 설계 방법론
- REST 원리를 따르는 시스템을 RESTful하다고 부름
- 자원을 정의하고 자원에 대한 주소를 지정하는 전반적인 방법을 서술

## JSON
- javascript 표기법에 따른 단순 문자열
- key-value 형태의 구조를 가지고 있음(python의 dictionary와 다름)
- 사람이 읽고 쓰기 쉽고 기계가 파싱(해석&분석)하고 만들어내기 쉽기 때문에 현재 API에서 가장 많이 사용하는 데이터 타입

## REST에서 자원 정의, 주소 지정 방법
1. 자원의 식별
- URI
2. 자원의 행위
- HTTP Method
3. 자원의 표현
- 자원과 행위를 통해 궁극적으로 표현되는 결과물
- JSON으로 표현된 데이터를 제공


# Reseponse
## 사전 준비
- migrate 
- fixtures load하여 초기 데이터 입력(실습 위해)

## Serialization
- 직렬화
- 여러 시스템에서 활용하기 위해 데이터 구조나 객체 상태를 나중에 재구성할 수 있는 포맷으로 변환하는 과정
- 어떠한 언어나 환경에서도 나중에 다시 쉽게 사용할 수 있는 포맷으로 변환하는 과정
- 변환 포맷은 json이 가장 보편적으로 쓰임


## 다양한 방법으로 JSON 데이터 응답
1. HTML 응답
- 문서(html) 한 장을 응답하는 서버 확인
2. JsonResponse()를 사용한 JSON 응답
- JSON 데이터를 응답하기
- JsonResponse 객체 활용하여 python 데이터 타입을 json으로 변환하여 응답 가능

3. Django Serializer 를 사용한 JSON 응답
- Django의 내장 HttpResonpose() 활용한 json 응답
- Django의 serialize()는 복잡한 데이터를 json 등 유형으로 쉽게 변환 할 수 있는 python 데이터 타입으로 만들어 줌

4. Django REST framework 사용한 JSON 응답
- 제일 중요!!!!!!!!

## Django REST framework (DRF)
- Django에서 Restful API 서버를 쉽게 구출할 수 있도록 도와주는 오픈소스 라이브러리
- DRF의 serialized는 Django의 Form 및 ModelForm 클래스와 매우 유사하게 작동

```python
# articles/serializers.py
from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
  class Meta:
    model = Article
    fields = '__all__'

# articles/views.py
@api_view(['GET'])
def article_json(request):
  articles = Article.objects.all()
  serializer = ArticleSerializer(articles, many=True)
  return Response(serializer.data)
```

# Django REST framework - Single model
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
  model = Article
  fields = ('__all__')
```

## GET-LIST
- 게시글 데이터 목록 조회하기
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

@api_list(['GET'])
def article_list(request,article_pk):
  articles = Article.objects.get(pk=article_pk)
  serializer = ArticleListSerializer(articles)
  return Response(serializer.data)
```