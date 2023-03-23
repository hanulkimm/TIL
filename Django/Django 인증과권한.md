# 인증과 권한

## 개요
- Django authentication system(인증 시스템)은 인증(Authentication)과 권한(Autorization)부여를 함께 제공(처리)
- 필수 구성은 settings.py에 이미 포함되어 있음
- Authentication(인증): 신원 확인, 사용자가 자신이 누구인지 확인하는 것
- Authorization(권한, 허가): 권한 부여, 인증된 사용자가 수행할 수 있는 작업 결정

## 사전 설정
- 두 번째 app acounts 생성 및 등록
- url 분리 및 매핑

# Custom User Model

## 개요
- Django는 현재 프로젝트에서 사용할 UserModel을 결정하는 `AUTH_USER_MODEL` 설정 값으로 Default User Model을 재정의할 수 있도록 함
### AUTH_USER_MODEL
- 프로젝트에서 User를 나타날 때 사용하는 모델
- 프로젝트가 진행되는 동안(모델을 만들고 마이그레이션 한 후) 변경할 수 없음
- 프로젝트 시작 시 설정하기 위한 것이며 참조하는 모델은 첫 번째 마이그레이션에서 사용할 수 있어야 함
  - 첫번째 마이그레이션 전에 확정 지어야 하는 값

## Custom User Model 대체하기
1. AbstractUser를 상속받는 커스텀 User 클래스 작성
```python
# accounts/models.py

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  pass
```
2. Django 프로젝트에서 User를 나타내는데 사용하는 모델은 방금 생성한 커스텀 User 모델로 지정
```python
# settings.py

AUTH_USER_MODEL = 'accounts.User'
```
3. admin.py에 커스텀 User 모델을 등록
- 기본 User 모델이 아니기 때문에 등록하지 않으면 admin site에 출력되지 않음
```python
from django.contrib import admin
from django.contrib.auth.adim import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)
```

## 데이터베이스 초기화
1. migrations 파일 삭제
- migrations 폴더 및 `__init__.py`는 삭제하지 않음
- 번호가 붙은 파일만 삭제
2. db.sqlite3 삭제
3. migrations 진행

# HTTP
- HTML 문서와 같은 리소스들을 가져올 수 있도록 해주는 프로토콜
- 웹에서 이루어지는 모든 데이터 교환의 기초
- 요청(requests): 클라이언트(브라우저)에 의해 전송되는 메세지
- 응답(response): 서버에서 응답으로 전송되는 이미지
## HTTP 특징
1. 비 연결 지향(connectionless)
- 서버는 요청에 대한 응답을 보낸 후 연결 끊음
- 예를 들어, 우리가 네이버 메인 페이지를 보고 있을 때 네어버 서버와 연결되어 있는 것이 아님
  - 서버는 우리에게 메인 페이지를 응답하고 연결을 끊은 것
2. 무상태 (stateless)
- 연결을 끊는 순간 클라이언트와 서버 간의 통신이 끝나며 상태 정보가 유지되지 않음
- 클라이언트와 서버가 주고받은 메시지들은 서로 완전 독립적

## 쿠키
- HTTP 쿠키는 상태가 있는 세션을 만들도록 해 줌
### 개념
- 서버가 사용자의 웹 브라우저에 전송하는 작은 데이터 조각
- 사용자가 웹사이트를 방문할 경우 해당 웹사이트의 서버를 통해 사용자의 컴퓨터에 설치되는 작은 기록 정보 파일
  - 브라우저(클라이언트)는 쿠키를 로컬에 KEY-VALUE의 데이터 형식으로 저장
  - 쿠키를 저장해 놓았다가, 동일한 서버에 재요청 시 저장된 쿠키를 함께 전송
- 쿠키는 두 요청이 동일한 브라우저에서 들어왔는지 아닌지를 판단할 때 주로 사용됨
  - 이를 이용해 사용자의 로그인 상태를 유지할 수 있음
  - 상태가 없는 HTTP 프로토콜에서 상태 정보를 기억 시켜 주기 때문
- 즉, 웹 페이지에 접속하면 웹 페이지를 응답한 서버로부터 쿠키를 받아 브라우저에 저장하고, 클라이언트가 같은 서버에 재요청 시마다 요청과 함께 저장해두었던 쿠키도 함께 전송

![image](https://user-images.githubusercontent.com/122726684/226777353-5250a806-b209-4ec9-bcaf-29fd1ec19817.png)

### 사용 목적
1. 세션 관리 (Session management)
- 로그인, 아이디 자동완성, 공지 하루 안 보기, 팝업 체크 등 정보 관리
2. 개인화
- 사용자 선호, 테마 등 설정
3. 트래킹
- 사용자 행동을 기록 및 분석

## 세션 (Session)
- 사이트와 특정 브라우저 사이의 상태를 유지시키는 것
- 클라이언트가 서버에 접속하면 서버가 특정 session id를 발급하고 클라이언트는 session id를 쿠키에 저장
  - 클라이언트가 다시 동일한 서버에 접속하면 요청과 함께 쿠키(session id가 저장된)를 서버에 전달
  - 쿠키는 요청 때마다 서버에 함께 전송되므로 서버에서 session id를 확인해 알맞는 로직을 처리
- session id는 세션을 구별하기 위해 필요하며, 쿠키에는 session id만 저장

## 쿠키 Lifetime (수명)
1. Session cookie
- 현재 세션이 종료되면 삭제됨
2. Persistent cookies
-  expires 속성에 지정된 날짜 혹은 max-age 속성에 지정된 기간이 지나면 삭제됨

# 로그인, 로그아웃, 회원가입, 회원 탈퇴, 정보 수정, 비밀번호 변경 하기
## LOGIN
- Session을 Create 하는 과정
- 사용자에 대한 세션을 생성하는 것
### AuthenticationForm
- 로그인을 위한 built-in form
  - 로그인 하고자 하는 사용자 정보 입력 받음
  - 기본적으로 username과 password를 받아 데이터가 유효한지 검증
  - request를 첫번째 인자로 취함
### Login
- `from django.contrib.auth import login as auth_login`
- login(request, user, backend=None)
- 인증된 사용자를 로그인 시키는 로직으로 view 함수에서 사용됨
- 현재 세션에 연결하려는 인증 된 사용자가 있는 경우 사용
- HttpRequest 객체와 User 객체 필요

```python
# accounts/urls.py

from django.urls import path
from . import views
app_name = 'accounts'
urlpatterns = [
  path('login/', views.login, name='login')
]

# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
def login(request):
  if request.method == "POST":
    form = AuthenticationForm(request, request.POST)
    if form.is_valid():
      auth_login(request, form.get.user())
      return redirect('articles:index')
  else:
    form = AuthenticationForm()

  context = { 'form':form }
  return render(request, 'accounts/login.html', context)
```
```html
{% extentds 'base.html' %}

{% block  content }
  <h1>로그인</h1>
  <form action="{% url 'accounts:login' %}" method="POST">
  {% csrt_token %}
  {{ form.as_p }}
  </form>
{% endblock  content }
```

### User

- 템플릿에서 인증 관련 데이터를 출력하는 방법

![image](https://user-images.githubusercontent.com/122726684/226792946-787bdd14-1e6b-4042-994c-b391c3f03cc8.png)
![image](https://user-images.githubusercontent.com/122726684/226793227-30209cf1-f79a-4703-9638-231e08adabbf.png)

## Logout
- Session을 Delete 하는 과정
- 세션을 클라이언트와 서버에서 삭제하는 것
### logout()
- `from django.contrib.auth import logout as auth_logout`
- HttpRequest 객체를 인자로 받고 반환 값이 없음
- 2가지 일 처리
  - 현재 요청에 대한 session data를 DB에서 삭제
  - 클라이언트 쿠키에서도 sessionid를 삭제
  - 이는 다른 사람이 동일한 웹 브라우저를 사용하여 로그인하고, 이전 사용자의 세션 데이터에 엑서스하는 것을 방지하기 위함 

```python
# accounts/urls.py

from django.urls import path
from . import views
app_name = 'accounts'
urlpatterns = [
  path('login/', views.login, name='login')
  path('logout/', views.logout, name='logout')
]

# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout as auth_logout
def logout(request):
  auth_logout(request)
  return redirect('articles:index')
```
```html
<!-- base.html -->
<body>
  <form action="{% url 'accounts:logout' %}" method="POST">
  {% csrt_token %}
  <input type="submit" value="Logout">
</body>
```

## 회원가입
- User를 Create하는 것이며 UserCreationForm built-in form을 사용
### UserCreationForm
- 주어진 username과 password로 권한이 없는 새 user를 생성하는 ModelForm
  
```python
# accounts/forms.py
## 회원가입에 사용하는 UserCreationForm이 우리가 대체한 커스텀 유저 모델이 아닌 기존 유저 모델로 인해 작성된 클래스이므로 수정하기

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
  class Meta(UsercreationForm.Meta):
    model = get_user_model()

# accounts/urls.py
app_name = 'accounts'
ulrpattern = [
  path('signup/', views.signup, name='signup'),
]
# accounts/views.py
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

def signup(request):
  if request.method=="POST":
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      auth_login(request, user) # 회원가입 후 바로 로그인 진행
      return redirerct('articles:index')
  else:
    form = UserCreationForm()
  context = {'form':form}
  return render(request, 'accounts/signup.html', context)
```
```html
{% extentds 'base.html' %}

{% block  content }
  <h1>회원가입</h1>
  <form action="{% url 'accounts:signup' %}" method="POST">
  {% csrt_token %}
  {{ form.as_p }}
  <input type='submit'>
  </form>
{% endblock  content }
```

## Custom user & Built-in auth forms
1. AbstractBaseUser의 모든 subclass와 호환되는 forms
- AuthenticationForm
- SetpasswordForm
- PasswordChangeForm
- AdminPasswordChangeForm
- User 모델을 대체하더라고 커스텀 하지 않아도 사용 가능
- 기존 User 모델을 참조하는 Form이 아니기 때문
2. 커스텀 유저 모델을 사용하려면 다시 작성하거나 확장해야 하는 forms
- UserCreationForm
- UserChangeForm

### 커스텀하기
```python
# accounts/forms.py
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
  class Meta(UsercreationForm.Meta):
    model = get_user_model()

class CustomUserChangeForm(UserChangeForm):
  class Meta(UserChangeForm.Meta):
    model = get_user_model()
    # 일반 사용자가 접근해서는 안 될 정보들(fields)까지 수정이 가능해지지 않도록 접근 가능한 필드를 조정해야 함
    fields = ('username', 'email', 'first_name', 'last_name')
```
### get_user_model():
- 현재 프로젝트에서 활성화된 사용자 모델(active user model)을 반환
- User 클래스를 직접참조하는 대신 get_user_model()을 사용해주면 커스텀 User 모델을 자동으로 반환해줌

## 회원 탈퇴
- DB에서 유저를 Delete하는 것과 같음
```python
# accounts/urls.py
app_name = 'accounts'
ulrpattern = [
  path('delete/', views.delete, name='delete'),
]
# accounts/views.py
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

def delete(request):
  request.user.delete() # 탈퇴 후
  auth_logout(request) # 로그아웃
  # 이 순서 바뀌면 안됨
  # 로그아웃 먼저 해버리면 해당 요청 객체 정보가 없어지기 때문에 탈퇴에 필요한 정보 또한 없어지기 때문에
  return redirect('articles:index')
```

## 회원정보 수정
- User를 Update
- UserChangeForm built-in form 사용
### UserChangeForm
- 사용자의 정보 및 권한을 변경하기 위해 admin 인터페이스에서 사용되는 ModelForm
- UserChangeForm 또한 ModelForm이기 때문에 instance 인자로 기존 user 데이터 정보를 받는 구조도 동일함
```python
# accounts/urls.py
app_name = 'accounts'
ulrpattern = [
  path('update/', views.update, name='update'),
]
# accounts/views.py

def update(request):
  if request.method=="POST":
    form = CustomUserChangeForm(request.POST, instance=request.user)
    if form.is_valid():
      form.save()
      return redirect('articles:index')
  else:
    form = CustomUserChangeForm(instance=request.user)
  context = {'form':form}
  return render(request, 'accounts/update.html', context)
```
```html
<!-- accounts/update.html -->
{% extentds 'base.html' %}

{% block  content }
  <h1>회원정보수정</h1>
  <form action="{% url 'accounts:update' %}" method="POST">
  {% csrt_token %}
  {{ form.as_p }}
  <input type='submit'>
  </form>
{% endblock  content }
```

## 비밀번호 변경
### PasswordChangeForm
- 사용자가 비밀번호를 변경할 수 있도록 하는 Form
- 이전 비밀번호를 입력하여 비밀번호를 변결할 수 있도록 함
### update_session_auto_hash()
- 암호 변경 시 세션 무효화 방지하기
- 비밀번호가 변경되면 기존 세션과의 회원 인증 정보가 일치하지 않게 되어버려 로그인 상태가 유지되지 못함
- 비밀번호는 잘 변경되었으나 기존 세션과의 회원 인증 정보가 일치하지 않기 때문
- 현재 요청과 새 session data가 파생 될 업데이트 된 사용자 객체를 가져오고 session data를 적절하게 업데이트 해줌
- 암호가 변경되어도 로그아웃 되지 않도록 새로운 password의 session data로 session을 업데이트함
```python
# accounts/urls.py
app_name = 'accounts'
ulrpattern = [
  path('password/', views.change_password, name='change_password' )
]
# accounts/views.py
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

def change_password(request):
  if request.method=="POST:
    form = PasswordChangeForm(request.user, request.POST)
    # form = PasswordChangeForm(user=request.user, data=request.POST)
    if form.is_valid():
      form.save()
      update_session_auth_hash(request, form.user)
      return redirect('articles:index')

  else:
    form = PasswordChangeForm(request.user)
  context = {'form':form}
  return render(request, 'accounts/change_password.html', context)
```
```html
<!-- accounts/password.html -->
{% extentds 'base.html' %}

{% block  content }
  <h1>비밀번호변경</h1>
  <form action="{% url 'accounts:change_password' %}" method="POST">
  {% csrt_token %}
  {{ form.as_p }}
  <input type='submit'>
  </form>
{% endblock  content }
```

## View decorators
- View decorators를 사용해 view 함수를 단단하게 만들기
- 기존에 작성된 함수에 기능을 추가하고 싶을 때, 해당 함수를 수정하지 않고 기능을 추가해주는 함수

![image](https://user-images.githubusercontent.com/122726684/227107172-6a41e67e-6507-4260-809e-bd0e77c65f5c.png)

## Allowed HTTP methods
- django.views.decorators.http의 데코레이터를 사용하여 요청 메서드를 기반으로 접근을 제한할 수 있음
- 일치하지 않는 메서드 요청이라면 405 Method Not Allowed를 반환
- 메서드 목록
1. `require_http_methods()`
- view 함수가 특정한 요청 method만 허용하도록 하는 데코레이터
```python
# views.py
from django.views.decorators.http import require_http_methods

@require_http_methods(['GET', 'POST'])
def crete(request):
  ~
```
2. `requires_POST()`

![image](https://user-images.githubusercontent.com/122726684/227108133-d211e7b4-8488-4f9c-95d8-36fe4fb78d64.png)
3. `require_safe()`
- require_GET이 있지만 django에서는 require_safe를 사용하는 것을 권장

## 로그인 사용자에 대한 접근 제한하기
###  `is_authenticated` 속성
- User model의 속성 중 하나
- 사용자가 인증 되었는지 여부를 알 수 있는 방법
- 모든 User 인스턴스에 대해 항상 True인 읽기 전용 속성
  - AnonymousUser에 대해서는 항상 False
- 일반적으로 request.user에서 사용 (request.user.is_authenticated)
- 권한과는 관련이 없으며 사용자가 활성화 상태이거나 유효한 세션을 가지고 있는지도 확인하지 않음

![image](https://user-images.githubusercontent.com/122726684/227111806-a3a1f4a6-99b7-4b7f-9746-0083af7a264c.png)
![image](https://user-images.githubusercontent.com/122726684/227112069-cac5c4b1-08d1-4eef-9267-fc7eaeda2d0e.png)
![image](https://user-images.githubusercontent.com/122726684/227111970-c649e9df-8229-47d7-bba0-8186d6b90262.png)