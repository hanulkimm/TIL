# DB 조작

## Grouping Data
### Aggregate function
- 집계 함수
- 값 집합의 최대값, 최소값, 평균, 합계 및 개수를 계산
- 값 집합에 대한 계산을 수행하고 단일 값을 반환
  - 여러 행으로부터 하나의 결과 값을 반환하는 함수
- 제공하는 함수 목록
  - AVG(), COUNT(), MAX(), MIN(), SUM()
- AVG(), MAX(), MIN(), SUM() 는 숫자를 기준으로 계산하기 때문에 반드시 ING 데이터 타입일 때만 사용 가능

- 예시:
  - `SELECT COUNT(*) FROM users;`
  - `SELECT AVG(balance) FROM users;`

### GROUP BY clause
```sql
SELECT column_1, aggregate_function(column_2) FROM table_name GROUP BY column_1, column_2;
```
- 특정 그룹으로 묶인 결과 생성
- SELECT 문에서 선택적으로 사용가능한 절
- SELECT 문의 FROM 절 뒤에 작성, WHERE 절이 포함된 경우, WHERE 절 뒤에 작성
- AS 키워드 사용하여 컬럼명을 임시로 변경하여 조회할 수 있음

- 예시: 각 지역별로 몇 명씩 살고 있는지 조회
  - `SELECT country, COUNT(*) AS number FROM users GROUP BY country;`
  - 위에서 COUNT(*) 대신에 어떤 컬럼을 넣어도 결과는 같음, 현재 쿼리에서는 그룹화된 country를 기준으로 카운트하는 것이기 때문에 어떤 컬럼을 카운트해도 전체 개수는 동일하기 때문
  

## Changing Data
### Insert
```sql
SELECT INTO table_name (column_1, column_2, ...) VALUES (values1, values2, ...)
```
- 새 행을 테이블에 삽입
- 만약 모든 컬럼에 대한 값 지정해주면 컬럼 목록은 선택 사항
- 여러 행을 한꺼번에 삽입도 가능
  
### Update
```sql
UPDATE table_name
SET column_1 = new_value_1,
  column_2 = new_value_2
WHERE 
  search_condition;
```
- WHERE 절 생략 시 모든 행에 있는 데이터를 업데이트 함
- ORDER BY, LIMIT 절 사용하여 업데이트 할 행 수를 지정할 수 있음

### Delete
```sql
DELETE FROM table_name
WHERE search_condition;
```
- 테이블에서 행 제거
- 한 행, 여러 행, 모든 행 삭제 가능
- WHERE 절 생략하면 모든 행 삭제 
- ORDER BY, LIMIT 절 사용하여 삭제할 행 수를 지정할 수 있음

# 정규형
## 개념
- 데이터베이스를 구조화하는 방법론
- 데이터의 중복을 최소화하고 일관성과 무결성을 보장하기 위함
- 데이터를 더 좋은 구조로 바꾸는 것을 정규화라고 함
- 관계형 데이터베이스의 경우 6개의 정규형이 있음
  
### 제 1 정규형
- 하나의 속성값이 복수형을 가지면 안됨
- 하나의 속성에는 값이 하나만 들어가야 함
- 아래 그림은 제 1정규형 위반
![image](https://user-images.githubusercontent.com/122726684/230248499-a91dbc58-6f1c-4725-8223-6ca0e4b6a95d.png)


### 제 2 정규형
- 테이블의 테마와 관련 없는 컬럼은 다른 테이블로 분리하는 것
- 부분 함수적 종속성(Partial Functional Dependency) 을 제거한 것
  - 키가 아닌 속성이 기본키의 일부분에 종속되는 것

![image](https://user-images.githubusercontent.com/122726684/230248785-b7d27570-8d55-4744-bf3b-fb70decf6186.png)

![image](https://user-images.githubusercontent.com/122726684/230248608-9d412cf2-d0c4-4505-a82c-6254c97c82b0.png)

### 제 3 정규형
- 다른 속성에 의존(종속)하는 속성은 따로 분리할 것

# JOIN

## 개념
- 두 개 이상의 테이블에서 데이터를 가져와 결합하는 것
- 조회를 하기 위해 테이블 연결하여 1개로 만들어야 함
- 종류: CROSS JOIN, INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL OUTER JOIN

## 테이블 합치기
![image](https://user-images.githubusercontent.com/122726684/230251485-e36e5527-9a15-498a-83be-3ae574190113.png)

### CROSS JOIN
- ` SELECT * FROM articles, users;`
   ![image](https://user-images.githubusercontent.com/122726684/230251619-9a6e459d-136d-4e06-b064-116131f31779.png)

- `SELECT * FROM articles.userID=users.rowID;`
- `SELECT * FROM userID=users.rowID;`

### INNER JOIN
```sql
SELECT * FROM articles INNER JOIN users ON userID=users.rowID;
```
![image](https://user-images.githubusercontent.com/122726684/230252301-60d334aa-8559-47e5-b3af-69beef62f5ae.png)

### LEFT(OUTER) JOIN
```sql
SELECT * FROM articles LEFT JOIN users ON userID=users.rowID;
```
![image](https://user-images.githubusercontent.com/122726684/230252415-d64251a4-5292-4897-9c06-4cfdcefb163f.png)
### RIGHT(OUTER) JOIN
```sql
SELECT * FROM articles RIGHT JOIN users ON userID=users.rowID;
```
![image](https://user-images.githubusercontent.com/122726684/230252490-c0054936-ee4e-486a-b9a3-d6e711470e72.png)