# 사용자가 입력한 각 자릿수를 더해 출력하는 코드 작성하기
s = input('숫자를 입력해주세요 : ')

# 1. 
length = len(s)

sum = 0

for i in range(length):
    sum = int(s[i]) + sum
print(sum)

# 2. 함수 이용해보기
def add_num(s):
    each_num = [int(i) for i in str(s)]
    return sum(each_num)

print(add_num(s))




