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
s.isalpha() # 알파벳 문자 여부(숫자 제외)
s.isdigit() # 숫자 여부
s.isspace() # 공백 여부, 문자열이 모두 공백이면 True
```
- 주요 문자열 변경 메서드
```python
s.replace(old,new, [,count]) # 바꿀 대상을 새로운 글자로 바꿔서 반환, count 개수 만큼 old를 new로 바꿈
s.strip([chars]) # 공백이나 특정 문자 제거, lstrip/rstrip 통해 왼쪽/오른쪽 제거, 특정문자 지정하면 그 문자 제거(모든 조합을 이용해서)
s.split() # 공백이나 특정 문자를 기준으로 분리
'seperator'.join([iterable]) # 구분자로 iterable를 합침, iterable에 문자열이 아닌 값이 있으면 TypeError 발생
s.capitalize() # 가장 첫 번째 글자를 대문자로 변경
s.title() # 띄어쓰기를 기준으로 각 단어의 첫글자는 대문자, 나머지는 소문자로 변환
s.swapcase() # 대문자를 소문자로, 소문자를 대문자로 변경

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
cafe.extend(['hollys'])
cafe.extend('cup')
print(cafe) # ['starbucks','coffeebean','hollys', 'c','u','p']
# 예시: 원하는 값을 모두 삭제.
a = [1, 2, 1, 3, 4]
target_value = 1
for i in range(a.count(target_value)):
    a.remove(target_value)
print(a)
```
- sort와 sorted 구분!
sort()는 원본을 변경하지만 sorted은 원본 변경이 없음, 새로운 변수에 지정을 해주어야 한다.
```python
# Sort()
numbers = [3,2,5,1]
result = numbers.sort()
print(numbers, result) # [1,2,3,5] None
# Sorted()
result = sorted(numbers)
print(numbers,result) # [3,2,5,1] [1,2,3,5]
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

## 순서가 없는 데이터 구조
### 셋 Set
- 중복되는 요소 없고 순서도 없음
- 주요 메서드
```python
s.copy() # 셋의 얕은 복사본 반환
s.add(x) # x가 셋에 없다면 추가
s.update(*others) # 셋에 여러 값을 추가
s.pop() # 셋에서 랜덤하게 항목 반환, 해당 항목 제거 후 셋이 비어있다면 에러
s.remove(x) # 항목 x를 셋에서 삭제, 항목 존재하지 않으면 에러
s.discard(x) # 항목 x를 셋에서 삭제, 항목 존재하지 않아도 에러 발생하지 않음
s.clear() # 모든 항목 제거
# 집합 관련 함수
s.isdisjoint(t) # 셋 s가 셋 t와 서로 같은 항목을 하나라도 갖지 않은 경우, True (서로소인가)
s.issubset(t) # 셋 s가 셋 t의 하위 셋인 경우, True반환
s.issuperset(t) # 셋 s가 셋 t의 상위 셋인 경우, True 반환
```

### 딕셔너리 Dictionary
- 주요 메세드
```python
d.clear() #모든 항목 제거
d.copy() # 딕셔너리의 얕은 복사본 반환
d.keys() # 모든 키를 담은 뷰 반환
d.values() # 모든 값을 담은 뷰 반환
d.items() # 모든 키-값 쌍을 담은 뷰 반환
d.get(k) # 키 k의 값 반환, 키 k가 딕셔너리에 없는 경우 None 반환
d.get(k,v) # 키 k의 값 반환, 없는 경우 v 반환
d.setdefault(k,v) # 키 k의 값 반환, 없는 경우 v 값 갖는 k를 dict에 삽입 후 v 반환
d.pop(k) # 키 k 값 반환하고 딕셔너리에서 삭제, 키 k가 없을 경우 에러 발생
d.pop(k,v) # 키 k 값 반환하고 딕셔너리에서 삭제, 키 k가 없을 경우 v 반환
d.update() # 딕셔너리의 값 매핑하여 업데이트

- 예시
my_dict = {'apple': '사', 'banana': '바나나'}
my_dict.update(appple='사과')
print(my_dict) #{'apple': '사과', 'banana': '바나나'}
```




