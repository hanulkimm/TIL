# Fixtures

## 개념
- fixture를 사용해서 모델에 초기 데이터를 제공함
- Django 프로젝트의 앱을 처음 설정할 때 동일하게 준비 된 데이터로 데이터베이스를 미리 채우는 것이 필요함
- Django에서 fixtures를 사용해 앱에 초기 데이터를 제공할 수 있음
- migrations와 fixtures를 사용하여 data와 구조를 공유하게 됨

## 정보 제공하기
### 생성(데이터 추출) - dumpdata
- `$ python manage.py dumpdata app_name.Model_name > filename.json`
- 응용 프로그램과 관련된 데이터베이스의 모든 데이터를 표준 출력으로 출력함
- 여러 모델을 하나의 json 파일로 만들 수 있음
- 예시: articles app의 articles 모델에 대한 data를 json 형식으로 저장하기

![image](https://user-images.githubusercontent.com/122726684/231471752-931fc3d4-d5cb-43c1-b8a3-9abc9a5d86b3.png)

![image](https://user-images.githubusercontent.com/122726684/231471823-1bebebcc-6602-4e4c-8ce1-82c2b62a4ea7.png)


### 로드(데이터 입력) - loaddata
- `$ python manage.py loaddata data.json`
- fixtures의 기본 경로: app_name/fixtures/
  - 모든 app의 디렉토리에서 fixtures 폴더 이후의 경로로 fixtures 파일을 찾음

- 예시
  - articles app에 fixtures 폴더만들고 모든 json파일을 이동시키기
  - db.sqlite3 파일 삭제 후 migrate 작업 진행
  - fixtures load하기: `$ python manage.py loaddata articles.json users.json comments.json`
  - loaddata 시 순서 중요!! user-article-comment순으로 data를 넣어야 오류가 발생하지 않음

- encoding error 발생 시
  - `$ python -Xutf8 manage.py dumpdata`