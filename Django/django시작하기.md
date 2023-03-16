# Django 시작하기

## 클라이언트 - 서버 구조
- 대부분의 웹 서비스는 클라이언트-서버 구조 기반으로 동작
- 클라이언트-서버 역시 하나의 컴퓨터
### 클라이언트
- 웹 사용자의 인터넷에 연결된 장치
- Chrome 같은 웹 브라우저
- 서비스 요청하는 주체 
### 서버
- 웹 페이지, 사이트 또는 앱을 저장하는 컴퓨터
- 클라이언트가 웹 페이지에 접근하려고 할 때 서버에서 클라이언트 컴퓨터로 웹 페이지 데이터를 응답해 사용자의 웹 브라우저에 표시됨 (주로 html)
- 요청에 대해 서비스를 응답하는 주체

## Django 따라하기
- 항상 공식문서 보기!!
```
$ pip install django==3.2.18 # django 설치
$ django-admin startproject firstpjt # 프로젝트 생성
$ python manage.py runserver # 서버 실행
$ python manage.py startapp articles # 앱 만들기
```

## 가상환경
```
python -m venv venv # 가상환경 생성
source venv/Scripts/activate # 가상환경 활성화
deactivate # 가상환경 비활성화
pip freeze > requirements.txt # 가상환경 패키지 목록 저장
pip install -r requirements.txt # 파일로부터 패키지 설치
```

## 프로젝트 구조
- `__init__.py`: python에게 이 디렉토리를 하나의 python 패키지로 다루도록 지시, 별도의 추가 코드 작성하지 않음
- `asgi.py` : django 애플리케이션이 비동기식 웹 서버와 연결 및 소통하는 것을 도움, 추후 배포시에 사용
- `settings.py` : django 프로젝트 설정 관리
- `urls.py` : 사이트의 url과 적절한 views의 연결을 지정
- `wsgi.py` : django 애플리케이션이 웹 서버와 연결 및 소통하는 것을 도움, 추후 배포시에 사용
- `manage.py` : django 프로젝트와 다양한 방법으로 상호작용하는 커맨트라인 유틸리티 

## Django Application
- 애플리케이션 생성 (일반적으로 이름은 복수형으로 작성)
` python manage.py startapp articles`
- 엡: 하나의 큰 기능 단위, 단일 앱으로 개발해도 괜찮음
### 애플리케이션 구조
- `admin.py`: 관리자용 페이지를 설정하는 곳
- `apps.py` : 앱의 정보가 작성된 곳, 별도의 추가 코드 작성하지 않음
- `models.py`: 앱에서 사용하는 Model을 정의하는 곳, MTV패턴의 M에 해당
- `tests.py`: 프로젝트의 테스트 코드를 작성하는 곳
- `views.py`: view함수들이 정의되는 곳, MTV패턴의 V에 해당

### 애플리케이션 등록 (!!!!!!!!중요!!!!!!!!!)
- 앱을 사용하기 위해서는 반드시 INSTALLED_APPS 리스트에 추가해줘야됨
```python
INSTALLED_APPS = [
  'articles',
  ~
]
```

**< 정리 >**
- Project:
  - 앱의 집합
  - 프로젝트에는 여러 앱이 포함될 수 있고 앱은 여러 프로젝트에 있을 수 있음
- Application
  - 실제 요청 처리하고 페이지 보여주는 등의 역할을 담당
  - 하나의 역할 및 기능 단위로 작성하는 것을 권장


