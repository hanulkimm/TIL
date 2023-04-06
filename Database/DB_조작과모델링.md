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