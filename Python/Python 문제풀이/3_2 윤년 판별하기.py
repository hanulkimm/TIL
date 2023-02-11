#윤년 판별하기
#해가 4의 배수이면서 100의 배수가 아니면 윤년, 400 배수면 윤년

year = int(input())

if year % 4 == 0 and year % 100 != 0:
    print('윤년')
elif year % 400 == 0:
    print('윤년')
else:
    print('윤년 아님') 

# 윤년 조건들 한 줄
if (year % 4 == 0 and year) or year % 400 == 0:
    print('윤년')
else:
    print('윤년 아니다')
