# 입력 예시
# 2015
# 8
# 31

# 출력 예시 
#경고 월요일입니다.
#{'년': 2015, '월': 8, '일': 31, '요일': '월요일'}


year = int(input())

import calendar
if calendar.isleap(year):
    print('윤년입니다. 연도를 다시 입력해주세요.')
    year = int(input())


calendar.prcal(year)

month = int(input())
day = int(input())

week = ['월요일','화요일','수요일','목요일','금요일','토요일','일요일'] 
if calendar.weekday(year,month,day) == 0:
    print('경고 월요일입니다.')
print(f"'년' : {year}, '월' : {month}, '일' : {day}, '요일' : {week[calendar.weekday(year,month,day)]}")




        
