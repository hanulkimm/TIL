# 자릿수 더하기 

# 반복문 활용않기
num = input()
def sum_of_digits(num):
    return sum( list(map(int,list(num))) )

print(sum_of_digits(num))


# 반복문 활용
num = input()
def sum_of_digits(num):
    total = 0
    for i in num:
        total += int(i)
    return total

print(sum_of_digits(num))

