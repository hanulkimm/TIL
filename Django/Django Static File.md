# Static Files

## Static File
- 응답할 때 별도의 처리 없이 파일 내용을 그대로 보여주면 되는 파일
- 파일 자체는 고정되어 있고 서비스 중에서도 추가되거나 변경되지 않고 고정 되어있음
## Media File
- 사용자가 웹에서 업로드하는 정적 파일(user-uploaded)
- 유저가 업로드한 모든 정적 파일
## 웹 서버와 정적 파일

![image](https://user-images.githubusercontent.com/122726684/227438214-ae5f9e1c-acf3-4adb-af0c-ace1fd534a5b.png)
![image](https://user-images.githubusercontent.com/122726684/227438557-35909f0e-fbff-4f75-85c3-4f89aa55d7e7.png)
- 웹 서버의 기본동작: 특정 위치(URL)에 있는 자원을 요청(HTTP request)받아서 응답(HTTP response)을 처리하고 제공(serving)하는 것
-  자원과 자원에 접근 가능한 주소 제공
   -  예를 들어, 사진 파일이 자원이고 해당 사진 파일을 얻기 위한 경로인 웹 주소(URL)이 존재
   -  웹 서버는 요청받은 URL로 서버에 존재하는 정적 자원을 제공함

## Static Files 구성하기
1. settings.py에서 STATIC_URL을 정의하기
2. 앱의 static 폴더에 정적 파일 위치하기
3. 템플릿에서 static 템플릿 태그를 사용하여 지정된 경로에 있는 정적 파일의 URL 만들기

### template tag
- `{% load %}`
  - load tag
  - 특정 라이브러리, 패키지에 등록된 모든 템플릿 태그와 필터를 로드
- `{% static '.png' %}`:
  - static tag
  - STATIC_ROOT에 저장된 정적 파일에 연결

## Static files 관련 Settings
1. STATIC_ROOT
2. STATICFILES_DIRS
- app/static/ 디렉토리 경로를 사용하는 것 외에 추갖거인 정적 파일 경로 목록을 정의하는 리스트
```python
# settings.py
STATICFILES_DIRS = [
  BASE_DIR / 'static', 
]
```
3. STATIC_URL
- STATIC_ROOT에 있는 정적 파일을 참조할때 사용할 URL
- 실제 파일이나 디렉토리가 아니며, URL로만 존재
```python
# settings.py
STATIC_URL = '/static/'
```

## STATIC file 가져오기
1. 기본 경로에 있는 static file 가져오기
- 1. articles/static/articles 경로에 이미지 파일 배치하기
- 2. static tag 사용해 이미지 파일 출력


![image](https://user-images.githubusercontent.com/122726684/226639194-9c0ee971-625a-4dcc-b332-51d89852ada1.png)

2. 추가 경로에 있는 static file 가져오기
- 1. 추가 경로 작성
```python
# settings.py
STATICFILES_DIRS = [
  BASE_DIR / 'static', 
]
```
- 2. static/경로에 이미지 파일 배치
- 3. static tag 사용해 이미지 파일 출력

![image](https://user-images.githubusercontent.com/122726684/226639694-6874f8c0-2607-4cb5-a7e9-58eb480e8cf4.png)

# Media Files

## ImageField()
- 이미지 업로드에 사용하는 모델 필드
- FileField를 상속받는 서브클래스이기 때문에 FileField의 모든 속성 및 메서드를 사용 가능
- 사용자에 위해 업로드 된 객체가 유효한 이미지인지 검사
- ImageField 인스턴스가 최대 길이가 100자인 문자열로 DB에 생성되며, max_length 인자를 사용하여 최대 길이를 변경 할 수 있음

## FileField()
- 파일 업로드에 사용하는 모델 필드

## 사전 단계
1. settings.py에서 MEDIA_ROOT, MEDIA_URL 설정
2. upload_to 속성을 정의하여 업로드 된 파일에 사용할 MEDIA_ROOT의 하위 경로를 지정

### MEDIA_ROOT
- Default = ' '(Empty String)
- 사용자가 업로드 한 파일(미디어 파일)들을 보관할 디렉토리의 절대 경로
- Django는 성능을 위해 업로드 파일은 데이터베이스에 저장하지 않음
  - DB에 저장되는 것은 파일 경로
- MEDIA_ROOT와 STATIC_ROOT는 반드시 다른 경로로 지정
```python 
# settings.py
MEDIA_ROOT = BASE_DIR / 'media'
```

### MEDIA_URL
- Default = ' '(Empty String)
- MEDIA_ROOT에서 제공되는 미디어 파일을 처리하는 URL
- 업로드 된 파일의 주소(URL)를 만들어 주는 역할
  - 웹 서버 사용자가 사용하는 public URL
- 비어 있지 않은 값으로 설정 한다면 반드시 slash로 끝내야 함
- MEDIA_URL과 STATIC_URL은 반드시 다른 경로로 지정
```python
# settings.py
MEDIA_URL = '/media/'
```

## 미디어 파일 제공하기
- 사용자로부터 업로드 된 파일이 프로젝트에 업로드 되고나서, 실제로 사용자에게 제공하기 위해서는 업로드 된 파일의 URL이 필요함
  - 업로드 된 파일의 URL: `settings.MEDIA_URL`
  - 위 URL을 통해 참조하는 파일의 실제 위치: `settings.MEDIA_ROOT`

![image](https://user-images.githubusercontent.com/122726684/227442417-7410e04c-a147-467a-a5ea-8f47a4008564.png)

## 미디어 파일 사용하기
- ImageField 사용하기 위해 Pillow 라이브러리 설치
- ImageField 작성
- ArticleForm에서 form tag에 enctype속성 변경
- views에서 request.FILES 추가
  - 파일 및 이미지는 request의 POST 속성 값으로 넘어가지 않고 FILES 속성 값에 담겨 넘어감

![image](https://user-images.githubusercontent.com/122726684/227444248-795e2039-1c42-4f8a-86f8-2dab61dc4fef.png)
![image](https://user-images.githubusercontent.com/122726684/227697718-38eb2ae5-5d06-4803-93fd-41b539e25605.png)
![image](https://user-images.githubusercontent.com/122726684/227697730-d99e4583-5df2-4cd6-8270-59f79adca057.png)

## 업로드 이미지 출력하기
- 업로드 된 파일의 상대 URL은 Django가 제공하는 url 속성을 통해 얻을 수 있음
- `article.image.url` : 업로드 파일의 경로
- `article.image` : 업로드 파일의 파일 이름
- 이미지 데이터가 있는 경우만 이미지 출력할 수 있도록 처리

![image](https://user-images.githubusercontent.com/122726684/227697919-6d68c602-834e-42e7-8f08-0f5e92e71e95.png)

### UPDATE
- enctype 속성값 추가
- 이미지 파일 담겨있는 request.FILES 추가 작성

![image](https://user-images.githubusercontent.com/122726684/227697942-3a4a0e02-9c48-4d0b-a18c-e97aaad12e2f.png)