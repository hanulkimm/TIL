# N:1 의 한계
## 예시 상황: 한 명의 의사에게 여러 환자 예약하기
- 2명의 의사와 환자, 환자는 서로 다른 의사에게 예약 가정

![image](https://user-images.githubusercontent.com/122726684/231049844-8cbaf737-c385-4cd3-bdf8-85c32d23fd8a.png)

![image](https://user-images.githubusercontent.com/122726684/231049911-b514f952-4913-44f0-b8bc-b38451a75c80.png)

- 1번 환자가 두 의사 모두에게 방문하려고 함
  - 동일한 환자지만 다른 의사에게 예약하기 위해서 객체를 하나 더 만들어서 예약 진행

![image](https://user-images.githubusercontent.com/122726684/231050007-8468716f-332b-467e-ac81-acb02d868f14.png)

## 중개 모델
- 환자모델에서 외래 키 삭제하고 별도의 예약 모델을 새로 작성
- 예약 모델은 의사와 환자에 각각 N:1 관계를 가짐

![image](https://user-images.githubusercontent.com/122726684/231050196-7cc3cb36-63c3-4337-91c9-1c9731ae74c7.png)

- 예약 만들기   

![image](https://user-images.githubusercontent.com/122726684/231050243-8cd0cbb8-e577-4a8c-bace-574ffb613398.png)

- 예약 정보 조회

![image](https://user-images.githubusercontent.com/122726684/231050307-9e6d44e8-904f-49f5-819c-9e260e43f374.png)

- 새로운 환자 예약

![image](https://user-images.githubusercontent.com/122726684/231050398-d6a7a2e1-16ee-4b23-8176-ae404cd4cbc6.png)


# ManyToManyField
## 개념
- `ManyToManyField(to, **options)`
- 모델필드의 RelatedManager를 사용하여 관련 개체를 추가,제거 또는 만들 수 있음
  - add(), remove(), create(), clear()

## Arguments
### 1. related_name
- target model이 source model을 참조할 때 사용할 manager name
- ForiegnKey의 related_name과 동일

### 2. through
- 중개 테이블을 직접 작성하는 경우, through 옵션을 사용하여 중개 테이블을 나타내는 Django 모델을 지정
- 일반적으로 중개 테이블에 추가 데이터를 사용하는 다대다 관계와 연결하려는 경우에 사용됨

### 3. symmetrical
- 기본값 : True
- True인 경우
  - _set 매니저 추가하지 않음
  - source 모델의 인스턴스가 target 모델의 인스턴스를 참조하면 자동으로 target 모델 인스턴스도 source 모델 인스턴스를 자동으로 참조하도록 함
- 대칭을 원하지 않는 경우 False로 설정
  - Follow 기능 구현에서 확인

## Related Manager
- N:1 혹은 M:N 관계에서 사용 가능한 문맥
- 같은 이름의 메서드여도 각 관계에 따라 다르게 사용 및 동작됨
  - N:1 에서는 target 모델 객체만 사용 가능
  - M:N 에서는 두 객체에서 모두 사용 가능
- 메서드 종류: add(), remove(), clear(), create(), set() 등

# M:N (Article-User)
## 개요
- Article 과 User의 M:N 관계 설정을 통한 좋아요 기능 구현하기

## LIKE
- ManyToField에 related_name 작성 
  - like_users 필드 생성 시 자동으로 역참조에는 .article_set 매니저가 생성됨
  - user.article_set.all() 시 user가 작성한 글들과 user가 좋아요 누른 글을 구분할 수 없게 됨
  - related_name 작성해야 함

![image](https://user-images.githubusercontent.com/122726684/231062846-1a4c55fc-b010-40c2-9344-ff9c1c29a947.png)

- User와 Article간 사용 가능한 related manager 정리
  - article.user : 게시글을 작성한 유저(N:1)
  - user.article_set : 유저가 작성한 게시글(N:1)
  - article.like_users: 게시글을 좋아요한 유저 (M:N)
  - user.like_article: 유저가 좋아요한 게시글(M:N)
  
![image](https://user-images.githubusercontent.com/122726684/231065670-e19ec7ae-fa8d-4ae1-bc6d-97476bbc3474.png)

- index template에 각 게시글에 좋아요 버튼 출력

![image](https://user-images.githubusercontent.com/122726684/231065758-55ba3294-4d45-4fcd-8fe6-d7a70117ed4a.png)

![image](https://user-images.githubusercontent.com/122726684/231065812-a586af19-c8b1-4471-ac22-eb8ddd791d7c.png)