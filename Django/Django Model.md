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

### Django shell
- ORM 관련 구문 연습을 위해 파이썬 쉘 환경 사용
` python manage.py shell_plus `

## QuerySet API

### Database API
- Django가 제공하는 ORM을 사용해 데이터베이스를 조작하느 방법
- Model을 정의하면 데이터를 만들고 읽고 수정하고 지울 수 있는 API를 제공
- API 구문
![image](https://user-images.githubusercontent.com/122726684/225658566-d3d7ae12-73d9-4a52-b863-30191d420721.png)