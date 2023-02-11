# 1. 세로로 출력하기
num = int(input())

for i in range(1,num+1):
    print(i)

# 2. 가로로 출력하기
num = int(input())
result = []

for i in range(1,num+1):
    result.append(i)
print(*result)

# 3. 거꾸로 세로로 출력하기
num = int(input())
numbers=list(range(num+1))
numbers.reverse()

for i in numbers:
    print(i)

# 4. 거꾸로 출력
num = int(input())
result = []

for i in range(1,num+1):
    result.append(i)
result.reverse()
print(*result)

# 5. N 줄 덧셈
num = int(input())

each_numbers = [i for i in range(1,num+1)]
print(sum(each_numbers))

# 6. 삼각형 출력하기
num = int(input())
for i in range(1,num+1):
    result = '*'*i
    print(result.rjust(num))

# 7. 중간값 찾기
numbers = [
    85, 72 , 38 , 80 , 69 , 65 , 68 , 96 , 22 , 49 , 67, 
    51, 61 , 63 , 87 , 66 , 24 , 80 , 83 , 71 , 60 , 64,
    52, 90 , 60 , 49 , 31 , 23 , 99 , 94 , 11 , 25 , 24,
]

numbers.sort() # 총 33개 

print(numbers[int((len(numbers)-1)/2)])
