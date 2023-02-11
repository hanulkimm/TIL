# 아이스 음료 주문이 몇 개 들어왔는지 확인하고 메뉴별 주문 수를 출력하기

from itertools import count


orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'


lst_orders = orders.split(',')

sum = 0  
for drinks in lst_orders:
    if '아이스' in drinks:
        sum = sum + 1
print(f'아이스 음료 주문 개수: {sum}개')  #아이스 음료 주문 개수

menu = list(set(lst_orders))
for drinks in menu:
    print(drinks,lst_orders.count(drinks)) #메뉴별 주문 수
    




