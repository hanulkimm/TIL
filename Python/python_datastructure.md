# 데이터 구조

## 의미
- 데이터 구조(자료 구조) : 각 데이터의 효율적인 저장,관리를 위한 구조를 나눠 놓은 것
- 공식문서를 자주 이용하자! 메서드를 구글링하기 전에 공식 문서 확인하는 습관 들이기!
- 메서드를 다 외울 생각보다 공식 문서를 통해 찾아보기!  

## 순서가 있는 데이터 구조
### 문자열 String Type
- str 타입은 변경불가능한 immutable
- 메서드를 통해 변경된 문자열을 새로 만들어서 반환(기존 문자열을 변경하는 것이 아님)
- 주요 문자열 조회/ 탐색 메서드 
```python
s.find(x) # x의 첫번째 위치 반환, 없으면 -1 반환
s.index(x) # x의 첫번째 위치 반환, 없으면 오류 발생
s.isupper(x) # 대문자 여부
s.islower(x) # 소문자 여부
```
- 주요 문자열 변경 메서드
```python
s.replace(old,new, [,count]) # 바꿀 대상을 새로운 글자로 바꿔서 반환
s.strip([chars]) # 공백이나 특정 문자 제거, lstrip/rstrip 통해 왼쪽/오른쪽 제거
s.split() # 공백이나 특정 문자를 기준으로 분리
'seperator'.join([iterable]) # 구분자로 iterable를 합침, iterable에 문자열이 아닌 값이 있으면 TypeError 발생

# 예시
print('!'.join('hello')) # s!s!a!f!y
print('Hello Python'.split()) # ['Hello', 'Python']
```

### 리스트 List
- 주요 메서드
```python
l.append(x) # 리스트 마지막 항목에 x 추가
l.insert(i,x) # 리스트 i index에 x 추가
l.extend(iterable) # iterable의 항목을 추가
l.remove(x) # 리스트 가장 왼쪽에 있는 x 제거
l.pop(i) # i번째 반환 후 제거, i 지정 안하면 마지막 항목 삭제하고 반환
l.clear() # 모든 항목 삭제
l.index(x) # x값 찾아 해당 index 반환
l.reverse() # 거꾸로 정렬
l.sort() # 정렬
l.count(x) # 항목 x 개수 반환

# 예시
cafe =['starbucks','coffeebean']
cafe.extend('cup')
print(cafe) # ['starbucks','coffeebean','c','u','p']
```

### 튜플 Tuple
- 불변 자료형, 담고 있는 값 변경할 수 없음
- 값에 영향을 미치지 않는 메서드만을 지원
- 리스트 메서드와 거의 동일, 항목 변경하는 메서드는 제외


## 연산자
### 멤버십 연산자
- 포함 여부 확인 in, not in
### 시퀀스형 연산자
- 산술 연산자 '+' , 반복 연산자 '*'
```python
# 리스트
[1,2] + ['a'] # [1,2,'a']
[0] * 3 # [0, 0, 0]
# 튜플
(1,2) + ('a',) # (1,2,'a')
(1,2) * 2 # (1,2,1,2)
# 문자열
'12' + 'b' #12b
'hi' * 2 # 'hihi'
# range -> 오류!!
```

