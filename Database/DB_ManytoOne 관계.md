# Database 관계

## 종류
1. 1:1
- One-to-one relationship
- 한 테이블의 레코드 하나가 다른 테이블의 레코드 단 한 개와 관련된 경우
2. N:1
- Many-to-one relationship
- 한 테이블의 0개 이상의 레코드가 다른 테이블의 레코드 한 개와 관련된 경우
- 기준 테이블에 따라(1:N, One-to-many-relationships)이라고도 함
- 여러 개의 주문 입장에서 각각 어떤 주문에 속해 있는지 표현해야 하므로 고객 테이블의 PK를 주문 테이블의 FK로 집어 넣어 관계 표현
- 예시: 고객이 여러 주문을 진행할 수 있음 

![image](https://user-images.githubusercontent.com/122726684/230803181-b6de3a56-07f6-4802-8503-6982dffc31de.png)

3. M:N
- Many-to-many relationship
- 한 테이블의 0개 이상의 레코드가 다른 테이블의 0개 이상의 레코드와 관련된 경우
- 양쪽 모두에서 N:1 관계를 가짐

## Django Relationship fields
1. OneToField() : One-to-one relationship
2. ForeignKey(to, on_delete, **options) : Many-to-one relationship
- Django 모델에서 관계형 데이터베이스의 외래 키 속성을 담당
- 2개의 필수 위치 인자 필요
  - 참조하는 model class
  - on_delete 옵션
3. ManyToManyField() : Many-to-one relationship


## Foreign Key
- 외래 키(외부 키)
- 관계형 데이터베이스에서 다른 테이블의 행을 식별할 수 있는 키
- 참조되는 테이블의 기본 키를 가리킴
- 참조하는 테이블의 행에는 참조되는 테이블에 나타나지 않는 값을 포함할 수 없음
- 참조하는 테이블 행 여러 개가 참조되는 테이블의 동일한 행을 참조할 수 있음
- 특징: 키를 사용하여 부모 테이블의 유일한 값을 참조, 외래 키의 값이 반드시 부모 테이블의 기본 키 일 필요는 없지만 유일한 값이어야 함

# N:1 (Comment-Article)
- Comment(N) - Article(1)
- Comment 모델과 Article 모델 간 관계 설정

![image](https://user-images.githubusercontent.com/122726684/230811684-402c06dd-9bfa-4b10-a28c-2e47fe9f3bd9.png)

## Comment Model
### 1. Comment 모델 정의
```python
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
```
- ForeignKey() 클래스의 인스턴스 이름은 참조하는 모델 클래스 이름의 단수형(소문자)로 작성하는 것을 권장
- related_name: ForeignKey 클래스의 선택 옵션, 역참조 시 사용하는 매니저 이름을 변경할 수 있음, 작성 후 migration 필요
  - `article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')`
- admin site에 Comment 모델 등록하기

### on_delete
- 외래 키가 참조하는 객체가 사라졌을 때, 외래 키를 가진 객체를 어떻게 처리할 지를 정의
- 데이터 무결성을 위한 중요한 설정
- 옵션 값
  - CASCADE: 부모 객체가 삭제됐을 때 이를 참조하는 객체도 삭제
  - PROTECT, SET_NULL, SET_DEFAULT 등

### 2. Migration 진행
- models.py에서 모델에 대한 수정사항이 발생했기 때문에 migration 진행
- ForeignKey 모델 필드로 인해 작성된 컬럼의 이름이 article_id인 것을 확인

### 3. 댓글 생성
`$ python manage.py shell_plus`

1. 댓글 생성  
     
![image](https://user-images.githubusercontent.com/122726684/230813184-a4d726d9-b273-4313-bb20-1463d14957a5.png)

![image](https://user-images.githubusercontent.com/122726684/230813225-0fb1f02c-dd2a-4402-8f81-8562edab65ff.png)    
2. 댓글 속성 값 확인  
![image](https://user-images.githubusercontent.com/122726684/230813286-e7be5fda-ddd9-4852-9ded-b617280f0af2.png)    
3. comment 인스턴스를 통한 article 값 접근  
![image](https://user-images.githubusercontent.com/122726684/230813369-7b345c37-f9b0-4dd6-85bc-36875aa2e55f.png)    
4. 댓글 하나 더 작성  
![image](https://user-images.githubusercontent.com/122726684/230813498-35031159-9797-4da6-bfdc-feaa0d0b3be8.png)    
5. 결과 확인    
![image](https://user-images.githubusercontent.com/122726684/230813544-1ad1ab34-ae5b-4b59-8c34-380cfed98f26.png)

## 관계 모델 참조
### Related manager
  - N:1, M:N 관계에서 역참조할 때 사용
### 역참조
- 나를 참조하는 테이블(나를 외래 키로 지정한)을 참조하는 것
- 본인을 외래 키로 참조 중인 다른 테이블에 접근하는 것
- N:1 관계에서는 1이 N을 참조하는 상황, 외래 키를 가지지 않은 1이 외래키를 가진 N을 참조
### comment_set
- `article.comment_set.method()`
- Article 모델이 Comment 모델을 역참조 할 때 사용하는 매니저
- Article클래스에는 Comment와 어떤 관계도 작성 되어 있지 않기 때문에 article.comment 형식으로 댓글 객체를 참조할 수 없음
- 반면에, 참조 상황(Comment-Article)에서는 실제 ForiegnKey 클래스로 작성한 인스턴스가 Comment 클래스의 클래스 변수이기 때문에 comment.article 형태로 작성 가능

- 예시:
`$ python manage.py shell_plus`
```
article=Article.objects.get(pk=1)
article.comment_set.all()
```

## Comment 구현
### CREATE
1. 외래 키 필드를 제외한 form 만들기

![image](https://user-images.githubusercontent.com/122726684/230816206-fe471d08-dddd-4529-b8a8-15951960eeca.png)    
2. views 페이지에서 CommentForm 넘겨주기  
![image](https://user-images.githubusercontent.com/122726684/230816722-986dde8f-ce8e-4351-81cc-a172fc75c307.png)    
3. detail 페이지에서 CommentForm 출력  
![image](https://user-images.githubusercontent.com/122726684/230816846-a234598a-ac6e-4c91-ae8d-66cc20a1db08.png)  
4. 댓글 받아오기  
![image](https://user-images.githubusercontent.com/122726684/230817747-4dc95406-11da-44cf-89c2-7b667611f105.png)
![image](https://user-images.githubusercontent.com/122726684/230817230-b0a6b933-d88d-4584-a429-52dca7d94445.png)
![image](https://user-images.githubusercontent.com/122726684/230817803-ee9478c6-ca7c-4d6b-88fa-6fa74940ac44.png)  
- save(commit=False): 아직 db에 저장되지 않은 인스턴스를 반환, 저장하기 전에 객체에 대한 사용자 지정 처리를 수행할 때 유용하게 사용
  
### READ

![image](https://user-images.githubusercontent.com/122726684/230818724-a634f68c-25d7-4878-b4d0-6548303a8649.png)
![image](https://user-images.githubusercontent.com/122726684/230818734-52bf2187-0fa2-414f-90a7-1d6533733214.png)

### DELETE
![image](https://user-images.githubusercontent.com/122726684/230819037-a7d6d8b4-0df4-40d7-b3ee-a55d4eb525b6.png)
![image](https://user-images.githubusercontent.com/122726684/230819122-a46f6e36-8c07-4611-847a-0699938ef04f.png)
![image](https://user-images.githubusercontent.com/122726684/230819144-8c4e8b21-0565-412a-a60a-8e46db6e0cc5.png)

## Comment 추가 사항
1. 댓글 개수 출력
- DTL filter: length 사용  
![image](https://user-images.githubusercontent.com/122726684/230819369-c5dee496-4c0b-4162-a148-4feb4978d948.png)    
- Queryset API: count() 사용  
![image](https://user-images.githubusercontent.com/122726684/230819426-d5fc66db-003a-413a-99ed-421d9d685c83.png)  
2. 댓글이 없는 경우 대체 컨텐츠 출력
![image](https://user-images.githubusercontent.com/122726684/230819558-f38f757f-f6f3-4b4e-966a-de00d0e0598a.png)

# N:1 (Article-User)
- Article 모델과 User 모델 간 관계 설정
- 0개 이상의 게시글은 1개의 회원에 의해 작성 될 수 있음

## User model 참조하기
1. settings.AUTH_USER_MODEL
- models.py의 모델 필드에서 User 모델을 참조할 때 사용
2. get_user_model()
- 현재 활성화된 User 모델 반환
- models.py가 아닌 다른 모든 곳에서 유저 모델을 참조할 때 사용

## 모델 관계 설정
![image](https://user-images.githubusercontent.com/122726684/230835050-6b78e1d3-a13b-4fff-9e89-8fa2c1591e94.png)

1. Article 모델에 User 모델을 참조하는 외래 키 작성   

![image](https://user-images.githubusercontent.com/122726684/230835729-96d4fe81-41f8-4be0-957a-62e404acd23b.png)

2. Migration 진행

![image](https://user-images.githubusercontent.com/122726684/230856258-c8b26315-5ada-4c84-bd19-090746ffc2d4.png)
- 첫번째 화면: 기본적으로 모든 컬럼은 NOT NULL 제약 조건이 있기 때문에 데이터가 없이는 새로 추가되는 외래 키 필드 user_id 가 생성되지 않음, 1 입력하고 enter 진행 
 

![image](https://user-images.githubusercontent.com/122726684/230856553-a776a806-470c-45b1-9e3f-b1719affd8a8.png)
- 두번째 화면: article의 user_id에 어떤 데이터를 넣을 것인지 직접 입력해야함, 1 입력하고 enter 진행, 기존에 작성된 게시글이 있다면 모두 1번 회원이 작성한 것으로 처리됨
  

## CREATE
- 인증된 회원의 게시글 작성 구현하기
- 작성하기 전 로그인 먼저 진행한 상태로 진행

1. ArticleForm의 출력 필드 수정하기  

![image](https://user-images.githubusercontent.com/122726684/230856990-ccf5afcd-1e4d-453b-8224-f854cf0d4a34.png)  
2. views 에서 게시글 작성 시 작성자 정보가 함께 저장될 수 있도록 save의 commit 옵션 활용  

![image](https://user-images.githubusercontent.com/122726684/230857133-ffa784b8-37f1-48bc-b5c4-9be82f1832e1.png)

## DELETE
- 게시글 삭제 시 작성자 확인


![image](https://user-images.githubusercontent.com/122726684/230857252-1d464a89-0468-4af1-b800-d992faa4aa65.png)

## UPDATE
- 수정을 요청하려는 사람과 게시글을 작성한 사람을 비교하여 본인의 게시글만 수정 할 수 있도록 함

![image](https://user-images.githubusercontent.com/122726684/230857420-40d99795-9dfa-4c1e-a706-34d328b7a22e.png)

- 해당 게시글의 작성자가 아니라면, 수정/삭제 버튼이 출력하지 않도록 함

![image](https://user-images.githubusercontent.com/122726684/230857540-428c86ab-ae07-4c0d-97da-fa014ac73b2a.png)

## READ
- index template과 detail template에서 각 게시글의 작성자 출력하기

![image](https://user-images.githubusercontent.com/122726684/230857647-de3764f3-2bce-491f-8814-991e0130ba39.png)

# N:1 (Comment-User)
![image](https://user-images.githubusercontent.com/122726684/231038420-6875f089-ba30-431a-8df4-205ba8f696b8.png)

- Comment 와 User 간 모델 관계 설정

![image](https://user-images.githubusercontent.com/122726684/231038530-54e921a9-e67c-4ca9-8ef9-bfb504882a31.png)

## CREATE
- 인증된 회원의 댓글 작성 구현하기
- 작성하기 전 로그인한 상태로 진행
- CommentForm의 출력 필드 수정

![image](https://user-images.githubusercontent.com/122726684/231038777-b07f69d8-c406-4c81-a90e-e1a3b3b89934.png)  
- 외래 키 데이터 누락 확인

![image](https://user-images.githubusercontent.com/122726684/231038868-bd4aa90e-5265-470a-8c8c-dc1d94f0a497.png)

## READ
- detail template에서 각 게시글의 작성자 출력

![image](https://user-images.githubusercontent.com/122726684/231038963-d7e2c82e-be9d-4d04-83ec-a5c135051957.png)

## DELETE
- 댓글 삭제 시 작성자 확인

![image](https://user-images.githubusercontent.com/122726684/231039107-09ef2d07-2cb9-4405-8966-98edc8839f81.png)

- 해당 댓글의 작성자가 아니라면, 삭제 버튼을 출력하지 않도록 함

![image](https://user-images.githubusercontent.com/122726684/231039201-23d11d3e-9fca-4d38-9cea-28e5632b3b0e.png)

## 인증된 사용자에 대한 접근 제한하기
- 인증된 사용자의 경우만 댓글 작성 및 삭제 가능

![image](https://user-images.githubusercontent.com/122726684/231039359-a91e796f-8e0b-4b09-a5f9-3fd7b379700f.png)

![image](https://user-images.githubusercontent.com/122726684/231039383-8daed11f-5615-45c5-b547-cce162ab2600.png)

- 비인증 사용자는 CommentForm 볼 수 없게 함

![image](https://user-images.githubusercontent.com/122726684/231039446-969e5fc7-3d58-4896-954f-79b14c2a0496.png)