# Database

## 개념
- DB
- DBMS
- Relational Database 관계형 데이터베이스 : 테이블 형태
- NoSQL Database 비관계형 데이터베이스: 관계형 데이터베이스의 한계를 극복하기 위해 조금 더 유연한 데이터베이스
  - 서브 데이터베이스로 두고 빠른 처리, 확장이 필요한 기능에서 사용하는 경우가 많음

## 관계형 데이터베이스(RDB)
- 데이터를 테이블, 행, 열 등으로 나누어 구조화 하는 방식
- 구조화해서 저장하므로 보다 체계적으로 데이터를 저장하고 관리할 수 있음
- 자료를 여러 테이블로 나누어서 관리하고 테이블 간 관계를 설정해 여러 데이터를 조작할 수 있음
- 데이터의 무결성(정확성, 일관성) 유지에 장점이 있음
- SQL을 사용하여 데이터를 조회하고 조작

### 관계형 데이터베이스의 구조
1. 스키마
   - 테이블의 구조
   - 데이터베이스에서 자료의 구조, 표현 방법, 관계 등 전반적인 명세 기술
2. 테이블
   - 필드와 레코드를 사용해 조직된 데이터 요소들의 집합
 - 1. 필드: 속성, 컬럼, 각 필드에는 고유한 데이터 형식 저장
 - 2. 레코드: 튜플, 행
 - 3. pk : 외래 키, 다른 테이블의 레코드를 식별할 수 있는 키, 다른 테이블의 기본 키를 참조


# SQL
## SQL이란
- 관계형 데이터베이스에서 데이터를 관리하기 위해 사용하는 언어

## SQL Commands
1. DDL(Data Definition Language)
2. DML(Data Manipulation Language)
3. DCL(Data Control Language)

![image](https://user-images.githubusercontent.com/122726684/229963036-a24b0e82-a152-4b4c-91f0-e55cc59de24d.png)

### SQL Syntax
- 모든 SQL문은 SELECT, INSERT, UPDATE 등과 같은 키워드로 시작하고, 하나의 statement는 세미콜론(;)으로 끝남
  - 세미콜론은 각 SQL문을 구분하는 표준 방법
- SQL키워드는 대소문자 구분하지 않음
  - 그러나 대문자 작성 권장

## DDL
- SQL 데이터 정의 언어를 사용하여 테이블 데이터베이스 개체를 만드는 방법을 학습
- DDL은 테이블 구조를 관리
  - CREATE, ALTER, DROP
### 사전 준비
1. 데이터베이스 mydb.sqlite3 파일 생성
2. DDL.sql 파일 생성
3. vscode 실행 후 ddl.sql 화면에서 마우스 우측 버튼 클릭
  - Use Database 선택
  - 목록에서 mydb.sqlite3 선택
  
## CREATE TABLE
- 데이터베이스에서 새 테이블을 만듦
```sql
CREATE TABLE table_name (
  column_1 data_type constraints,
  column_2 data_type constraints,
  column_3 data_type constraints
);
```

- 예시:
1. contacts 테이블 생성
```sql
CREATE TABLE contacts (
  name TEXT NOT NULL,
  age INTEGER NOT NULl,
  email TEXT NOT NULL UNIQUE
);
```
2. query 실행
- 실행하고자 하는 명령문에 커서를 두고 마우스 우측 버튼 --> Run Selected Query 선택
- 모든 명령문 선택할 필요 없이 실행하고자 하는 명령문 안에 커서가 올라가 있으면 가능
3. 쿼리 실행 후 테이블 및 스키마 확인

### SQLite Data Types
1. NULL
- 정보가 없거나 알 수 없음을 의미
2. INTEGER
- 정수
- 크기에 따라 0, 1, 2, 3, 4, 6 또는 8바이트와 같은 가변 크기를 가짐
3. REAL
- 실수
- 8바이트 부동 소수점을 사용하는 10진수 값이 있는 실수
4. TEXT
- 문자 데이터
5. BLOB(Binary Large Object)
- 입력된 그래도 저장된 데이터 덩어리
- 바이너리 등 멀티미디어 파일
  - 예시: 이미지

### 참고
- Boolean type: SQlite에는 별도의 Boolean 타입이 없음, 대신 정수 0(false)과 1(true)로 저장
- Type Affinity: 특정 컬럼에 저장된 데이터에 권장되는 타입, 데이터 타입 작성 시 SQlite의 5가지 데이터 타입이 아닌 다른 데이터 타입을 선언한다면, 내부적으로 각 타입의 지정된 선호도에 따라 5가지 선호도로 인식됨
  - 다른 데이터베이스 엔진 간의 호환성을 최대화, 정적이고 엄격한 타입을 사용하는 데이터베이스의 SQL문을 SQlite에서도 작동하도록 하기 위함
![image](https://user-images.githubusercontent.com/122726684/229966132-7daabb9d-a331-4e62-9696-9a669b8429dd.png)

### Constraints
- 입력하는 자료에 대해 제약을 정함
- 제약에 맞지 않다면 입력이 거부됨
- 사용자가 원하는 조건의 데이터만 유지하기 위한 즉, 데이터의 무결성을 유지하기 위한 보편적인 방법으로 테이블의 특정 컬럼에 설정하는 제약
1. NOT NULL
- 컬럼이 NULL값을 허용하지 않도록 지정
- 기본적으로 테이블의 모든 컬럼은 NOT NULL 제약 조건을 명시적으로 사용하는 경우를 제외하고는 NULL 값을 허용
2. UNIQUE
- 컬럼의 모든 값이 서로 구별되거나 고유한 값이 되도록 함
3. PRIMARY KEY
- 테이블에서 행의 고유성을 식별하는데 사용되는 컬럼
- 각 테이블에는 하나의 기본 키만 있음
- 암시적으로 NOT NULL 제약 조건이 포함되어 있음
- INTEGER 타입에만 사용 가능
4. AUTOINCREMENT
- 사용되지 않은 값이나 이전에 삭제된 행의 값의 재사용 방지
- INTEGER PRIMARY KEY 다음에 작성하면 해당 rowid를 다시 재사용하지 못하도록 함
- Django에서 테이블 생성 시 id컬럼에 기본적으로 사용하는 제약 조건
5. 기타
   
## ALTER TABLE
- 기본 테이블의 구조를 수정(변경)
1. ALTER TABLE   
`ALTER TABLE table_name RENAME TO new_name;`  
2. REMANE COLUMN  
`ALTER TABLE table_name RENAME COLUMN column_name TO new_column_name;`
3. Add new column to a table  
`ALTER TABLE table_name ADD COLUMN column_definition;`

- 예시: `ALTER TABLE contacts ADD COLUMN address TEXT NOT NULL;`
- 에러 발생 시: 
  - 이전에 이미 작성된 데이터들은 새롭게 추가되는 컬럼에 값이 없기 때문에 NULL이 작성됨
- 그러나 새로 추가되는 컬럼에 NOT NULL 제약 조건이 있기 때문에 기본 값 없이는 추가될 수 없다는 에러 발생
- 해결: DEFAULT 제약 조건을 주어 해결할 수 있음, `ALTER TABLE contacts ADD COLUMN address TEXT NOT NULL DEFAULT 'no address'`

4. Delete a column  
` ALTER TABLE table_name DROP COLUMN column_name;`
- 삭제 못하는 경우
  - 컬럼이 다른 부분에서 참조되는 경우
  - PRIMARY KEY인 경우
  - UNIQUE 제약 조건이 있는 경우

## DROP TABLE
- 데이터 베이스에서 테이블 제거
- `DROP TABLE table_name;`
- 한 번에 하나의 테이블만 삭제 가능
- 여러 테이블을 제거하려면 여러 DROP TABLE문을 실행해야 함
- 실행 취소하거나 복구할 수 없음
- 