# Django Model
![image](https://user-images.githubusercontent.com/122726684/225648668-1ec6d6ea-0ef0-4ac5-b868-4d6813ca0243.png)
## Database
- 체계화된 데이터의 모임
- 검색 및 구조화 같은 작업을 보다 쉽게 하기 위해 조직화된 데이터를 수집하는 저장 시스템

### Database 기본 구조
1. 스키마
- 뼈대
2. 테이블(Table)
- 필드와 레코드를 사용해 조직된 데이터 요소들의 집합, 관계라고도 부름
3. 필드: 속성 또는 열, 각 필드에는 고유한 데이터 형식 지정
4. 레코드: 튜플 또는 행, 테이블 데이터 저장
5. PK(Primary Key): 레코드의 기본 값, 중복 불가능
6. 쿼리: 데이터를 조회하기 위한 명령어, 조건에 맞는 데이터 추출하거나 조작하는 명령어
   
## Model
- 저장된 데이터베이스의 구조
- Model을 통해 데이터에 접근하고 조작
- 모델 클래스 1개 = 데이터베이스 테이블 1개
### model.py 작성하기
- 모델 클래스 작성 = 테이블의 스키마 정의
```python
# articles/models.py
class Arcticle(models.Model):
  title = models.CharField(max_length=10)
  content = models.TextField()
```
- 각 모델은 django.models.Model 클래스의 서브 클래스
- 클래스 상속 기반 형태의 Django 프레임워크 개발
- models 모듈을 통해 DB 필드 타입 정의
  - Django Model Field: 테이블의 필드(컬럼)에 저장할 데이터 유형을 정의

## Migrations
- Django가 모델에 생긴 변화(필드 추가, 수정 등)를 실제 DB에 반영하는 방법
### 주요 명령어
1. makemigrations
- 모델의 변경 사항에 대한 새로운 migration 만들 때 사용  
`$ python manage.py makemigrations`
- 만약 지우고 싶다면, 폴더와 init.py를 제외하고 delete 해야함

2. migrate
- makemigrations로 만든 설계도를 실제 db에 반영하는 과정
- 결과적으로 모델의 변경사항과 데이터베이스를 동기화
`$ python manage.py migrate`

## ORM
- Object-Relational-Mapping
- SQL을 사용하지 않고 데이터베이스를 조작할 수 있게 만들어주는 매개체

![image](https://user-images.githubusercontent.com/122726684/225653650-ff4debe1-311c-4e82-9b7d-86eca6b8049b.png)


## 사전 준비
### 테이블 데이터 확인
1. SQLite 설치
2. db.sqllite3 파일 우클릭 - Open Database
3. 좌측 하단 SQLITE EXPLORER 확인

### 외부 라이브러리 설치 및 설정
```bash
$ pip install ipython
$ pip install django-extensions
# settings.py
INSTALLED_APPS = [
  'django_extensions', # 추가해주기
]
$ pip freeze > requirements.txt
```

## Django shell
- ORM 관련 구문 연습을 위해 파이썬 쉘 환경 사용
` python manage.py shell_plus `

## QuerySet API
### Database API
- Django가 제공하는 ORM을 사용해 데이터베이스를 조작하는 방법
- Model을 정의하면 데이터를 만들고 읽고 수정하고 지울 수 있는 API를 제공
- API 구문


![image](https://user-images.githubusercontent.com/122726684/225658566-d3d7ae12-73d9-4a52-b863-30191d420721.png)
- objects manager
  - django는 기본적으로 모든 django 모델 클래스에 대해 objects라는 manager 객체를 자동으로 추가
  - 이를 통해 특정 데이터 조작 가능
  - DB를 python class로 조작할 수 있도록 여러 메서드를 제공하는 manager
- Query
  - 데이터베이스에 특정한 데디터를 보여달라는 요청
  - 파이썬으로 작성한 코드가 ORM에 의해 SQL로 변환되어 데이터베이스에 전달되며, 데이터베이스의 응답 데이터를 ORM이 QuerySet이라는 자료 형태로 변환하여 우리에게 전달
- QuerySet 
  - 데이터베이스에게서 전달 받는 객체 목록(데이터 목록)
  - django orm을 통해 만들어진 자료형이며 필터를 걸거나 정렬 등을 수행할 수 있음
  - objects manager를 사용하여 복수의 데이터를 가져오는 queryset method를 사용할 때 반환되는 객체
  - 단, 데이터베이스가 단일한 객체를 반환 할 때는 QuerySet이 아닌 모델의 인스턴스로 반환됨

# CRUD
- Create/ Read/ Update/ Delete
- 대부분의 컴퓨터 소프트웨어가 가지는 기본적인 데이터 처리 기능 4가지를 묶어서 일컫는 말
## Create: 데이터 객체를 만드는(생성하는) 3가지 방법
1. 첫번째 방법  
 - article = Article()
 - article.title
 - article.save()
  
![image](https://user-images.githubusercontent.com/122726684/226249927-331227c8-491e-4d70-bc3e-e6984a7b8a93.png)
![image](https://user-images.githubusercontent.com/122726684/226250020-cbc64fdc-a553-4b73-b998-2e341cba70a2.png)
![image](https://user-images.githubusercontent.com/122726684/226250084-56b6cb9c-bc55-4853-82fb-69ab76296747.png)

2. 두번째 방법 
- 인스턴스 생성 시 초기 값과 함께 작성하여 생성

![image](https://user-images.githubusercontent.com/122726684/226250240-daae7b2c-2d9d-47b6-bea5-80352cdac2a0.png)
3. 세 번째 방법
- QuerySet API 중 create() 메서드 활용
```
Article.objects.create(title='third', content='django')    
<Article: Article object (3)>
```
- .save()
  - 객체를 데이터베이스에 저장함
  - 데이터 생성 시 save를 호출하기 전에는 객체의 id 값은 None
  - id 값은 django가 아니라 db에 계산되기 때문
  - 단순히 모델 클래스를 통해 인스턴스를 생성하는 것은 db에 영향을 미치지 않기 때문에 반드시 save를 호출해야 테이블에 레코드가 생성됨

## READ
### all()
- QuerySet return
- 전체 데이터 조회

![image](https://user-images.githubusercontent.com/122726684/227150744-500cead7-3dd6-4b1e-bf49-8ad95da84a6b.png)
### get()
- 단일 데이터 조회
- 객체를 찾을 수 없다면 DoesNotExist 예외를 발생시키고, 둘 이상의 객체를 찾으면 MultipleObjectsReturned 예외를 발생시킴
- 위의 특성 때문에 primary key와 같이 고유성(uniqueness)을 보장하는 조회에서 사용해야 함

![image](https://user-images.githubusercontent.com/122726684/227151084-865c99e0-e347-4f67-bc02-97d3457f171a.png)

### filter()
- 지정된 조회 매개 변수와 일치하는 객체를 포함하는 새 QuerySet을 반환
- 조회된 객체가 없거나 1개여도 QuerySet을 반환
  
![image](https://user-images.githubusercontent.com/122726684/227151298-b93784e7-9149-480b-8831-581af5041c6f.png)

### Field lookups
- 특정 레코드에 대한 조건을 설정하는 방법
- QuerySet 메서드 filter(), exclude(), get()에 대한 키워드 인자로 지정됨

![image](https://user-images.githubusercontent.com/122726684/227209385-4c22c01b-4c9e-4dac-8fc0-51c7b6a7170c.png)

## UPDATE
1. 수정하고자 하는 article 인스턴스 객체를 조회 후 반환 값을 저장
2. article 인스턴스 객체의 인스턴스 변수 값을 새로운 값으로 할당
3. save() 인스턴스 메서드 호출

![image](https://user-images.githubusercontent.com/122726684/227210364-d1b216e5-2bca-44c0-8980-ca5810053600.png)

## DELETE
1. 삭제하고자 하는 artice 인스턴스 객체를 조회 후 반환 값을 저장
2. delete() 인스턴스 메서드 호출

![image](https://user-images.githubusercontent.com/122726684/227210572-5a2e355d-c7fe-4710-b140-7224d9072093.png)