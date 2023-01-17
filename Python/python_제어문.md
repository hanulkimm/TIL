# **Python 제어문**

## 조건문
### 기본 형식
```
if 조건 ==  True:
    #Run this code
else:
    #Run this code
```
- 예시: 홀수, 짝수 구분
```
num = int(input())
if num % 2:  # num % 2 == 1
    print('odd')
else: 
    print('even')  
```    
   

### 복수 조건문
```
if 조건:
    # Code
elif 조건:
    # Code
elif 조건:
    # Code
else:
    # Code
```
### 중첩 조건문
- 들여쓰기 조심하기
```
if 조건:
    # Code
    if  조건:
        # Code
else:
    # Code
```

### 조건 표현식

```
true인 경우 값 if 조건 else false인 경우 값
```

- 예시: 홀수, 짝수 구분
```
num = int(input())
result = 'odd' if num % 2 else 'even'
print(result)
```

## 반복문
### While 문
- 특정 조건(조건이 참)을 따를 때, 반복하여 코드 실행
- 종료 조건 코드 통해 종료해야 함
```
while 조건:
    # Code
```
- 예시
```
a = 0
while a < 5:
    print(a)
    a += 1
print('끝')
```

### For 문
- 반복 횟수를 알 때(가늠 가능할 때), 유용
- 별도 종료 조건 필요 없음
```
for 변수명 in iterable:
    # Code
```
- 예시: 사용자 입력 문자의 한 글자씩 출력
```
chars = input()
for char in chars:
    print(char)
```
- Dictionary 순회: 기본적으로 key를 순회
    - 추가 메서드 활용하여 순회
      - keys(): key로 구성된 결과
      - values(): value로 구성된 결과
      - items(): (key,value)의 튜플로 구성된 결과

```
grades = {'Anna' : 80, 'Tom' : 90}
print(grades.keys())  #dict_keys(['Anna', 'Tom'])
for students in grades.items():
    print(students,grades)
```
- enumerate 순회: (index,value) 형태의 tuple로 구성된 열거 객체 반환
```
members = ['kim','park','lee']
for idx, number in enumerate(members):
    print(idx, number)
```

- List Comprehension: 
  - 리스트를 간결하게 생성하는 방법
```
code for 변수 in iterable
code for 변수 in iterable if 조건식 
```
 
- Dictionary Comprehension
  - 딕셔너리를 간결하게 생성하는 방법
```
{key:value for 변수 in iterable}
{key:value for 변수 in iterable if 조건식}
```

## 반복문 제어
- Break: 반복문 종료
- Continue: 이후 코드 블록 수행 않고 다음 반복 수행
- For-else: 끝까지 for 반복문 실행 후 else 문 실행
    - break통해 중간에 종료되는 경우, else문 실행하지 않음
- Pass: 아무것도 하지 않음
- 예시 : 5의 배수 프린트 말고 5의 배수가 아니면 프린트
```
for i in range(100):
    if i % 5 == 0
        continue
    print(i)
```


> 관련 문제 풀이
1. 윤년 판별하기 
- 윤년 판별 조건: 
    - 해가 4의 배수이면서 100의 배수가 아니면 윤년
    - 400의 배수이면 윤년
```
year = int(input())
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print('윤년')
else:
    print('윤년 아님')
```

2. 끝말잇기 
- 끝말잇기 리스트 주어질 때, 탈락하는 사람 구하기
- 끝말잇기 틀리거나 중복되는 단어 말할 때, 탈락
```
words = ["python" , "nap", "python" , "nerd" , "dune", "egg"]

for idx in range(1,len(words)):
    if words[idx][0] != words[idx-1][-1]:
        print(f'{idx+1}번째 사람 탈락')
        break
    elif words[idx] in words[:idx]:
        print(f'{idx+1}번째 사람 탈락')

```
- 또 다른 문제 풀이 (Flag 이용하기)
```
words = ["python" , "nap", "python" , "nerd" , "dune", "egg"]

flag = False
for idx in range(1, len(words)):
    
    if words[idx-1][-1] != words[idx][0]:
        print('실패', idx, words[idx])
        flag = True
    else:
        for sub_idx in range(inx):
            pre_word = words[sub_idx]
            me_word = words[idx]
            if pre_word == me_word:
                print('실패', idx, words[idx])
                flag = True
                break
    if flag:
        break
```