# 1. 간단한 N의 약수
# 정수 N의 약수를 오름차순으로 출력하는 프로그램을 작성하시오.

N = int(input())

result = []

for i in range(1,N+1):
    if N % i == 0:
        result.append(i)
    else:
        continue
print(result)


# 2. List의 합 구하기
# 정수로만 이루어진 list 를 전달 받아 해당 list 의 모든 요소들의 합을 반환하는 list_sum 함수를 built in 함수인 sum() 함수를 사용하지 않고 작성하시오
lst = [1,2,3,4,5]

def list_sum(lst):
    total = 0
    for i in range(len(lst)):
        total = total + lst[i]
    return total

print(list_sum(lst))

# 3. Dictionary로 이루어진 List의 합 구하기
# Dictionary 로 이루어진 list 를 전달 받아 모든 dictionary 의 'age' key 에 해당하는 value들의 합을 반환하는 dict_list_sum 함수를 built in 함수인 sum() 함수를 사용하지 않고 작성하시오
my_dict = [{'name': 'kim', 'age': 12},
            {'name': 'lee', 'age':4}]


def dict_list_sum(my_dict):
    dic1 = my_dict[0]
    dic2 = my_dict[1]
    return dic1['age'] + dic2['age']
print(dict_list_sum(my_dict))

# 4. 2차원 List의전체 합 구하기
# 정수로만이루어진 2 차원 list 를 전달 받아 해당 list 의 모든 요소들의 합을 반환하는 all_list_sum 함수를 built in 함수인 sum() 함수를 사용하지 않고 작성하시오

#list comprehension 이용하기

lst = [ [1], [2,3], [4,5,6], [7,8,9,10] ]
def all_list_sum(lst):
    result= []
    for inner_list in lst:
        for data in inner_list:
            result.append(data)
    
    total = 0
    for i in result:
        total = total + i
    return(total)
  
print(all_list_sum(lst))


# 5. 숫자의 의미
# 정수로 이루어진 list 를 전달 받아 , 각 정수에 대응되는 아스키 문자를 이어붙인 문자열을 반환하는 get_secret_word 함수를 작성하시오 .
# ''.join() 사용
lst = [83, 115, 65, 102, 89]
def get_secret_word(lst):
    word = []
    for i in lst:
        word.append(chr(i))
    return word

print(''.join(get_secret_word(lst)))

# 6. 내 이름은 몇일까?
#문자열을 전달 받아 해당 문자열의 각 문자에 대응되는 아스키 숫자들의 합을 반환하는 get_secret_number 함수를 작성하시오 . 단 , 문자열은 A~Z, a~z 로만 구성되어 있다
word = input()

def get_secret_number(word):
    sum = 0
    for char in word:
        sum = sum + ord(char)
    return sum
print(get_secret_number(word))

# 7. 강한 이름
# 문자열 2 개를 전달 받아 두 문자열의 각 문자에 대응되는 아스키 숫자들의 합을 비교하여 더 큰 합을 가진 문자열을 반환하는 get_strong_word 함수를 작성하시오.
# 단, 두 문자열의 아스키 숫자의 합이 같은 경우 , 둘 다 반환하세요

a,b = input().split()

def get_strong_word(a,b):
    sum1 = 0
    sum2 =0
    for char in a:
        sum1 += ord(char)
    
    for char in b:
        sum2 += ord(char)
    
    if sum1 > sum2:
        return a
    elif sum1 < sum2:
        return b
    else:
        return a,b 

print(get_strong_word(a,b))


