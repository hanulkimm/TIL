# Static Files

## Static File
- 응답할 때 별도의 처리 없이 파일 내용을 그대로 보여주면 되는 파일
- 파일 자체는 고정되어 있고 서비스 중에서도 추가되거나 변경되지 않고 고정 되어있음
## Media File
- 사용자가 웹에서 업로드하는 정적 파일(user-uploaded)
- 유저가 업로드한 모든 정적 파일

## Static Files 구성하기
1. settings.py에서 STATIC_URL을 정의하기
2. 앱의 static 폴더에 정적 파일 위치하기
3. 템플릿에서 static 템플릿 태그를 사용하여 지정된 경로에 있는 정적 파일의 URL 만들기

### template tag
- `{% load %}`: 특정 라이브러리, 패키지에 등록된 모든 템플릿 태그와 필터를 로드
- `{% static '.png' %}`: STATIC_ROOT에 저장된 정적 파일에 연결

## Static files 관련 Settings
1. STATIC_ROOT
2. STATICFILES_DIRS
- app/static/ 디렉토리 경로를 사용하는 것 외에 추갖거인 정적 파일 경로 목록을 정의하는 리스트
```python
STATICFILES_DIRS = [
  BASE_DIR / 'static', 
]
```
3. STATIC_URL
- STATIC_ROOT에 있는 정적 파일을 참조할때 사용할 URL
- 실제 파일이나 디렉토리가 아니며, URL로만 존재

## STATIC file 가져오기
1. 기본 경로에 있는 static file 가져오기
- 1. articles/static/articles 경로에 이미지 파일 배치하기
- 2. static tag 사용해 이미지 파일 출력


![image](https://user-images.githubusercontent.com/122726684/226639194-9c0ee971-625a-4dcc-b332-51d89852ada1.png)

2. 추가 경로에 있는 static file 가져오기
- 1. 추가 경로 작성
```python
STATICFILES_DIRS = [
  BASE_DIR / 'static', 
]
```
- 2. static/경로에 이미지 파일 배치
- 3. static tag 사용해 이미지 파일 출력

![image](https://user-images.githubusercontent.com/122726684/226639694-6874f8c0-2607-4cb5-a7e9-58eb480e8cf4.png)