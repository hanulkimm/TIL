# n = 2일 때,
#     print('*' * (4 * n - 3))
#     print('*' + ' ' * (4 * n - 3 - 2) + '*')
#     print('*' + ' ' + '*' + ' ' + '*')
#     print('*' + ' ' * (4 * n - 3 - 2) + '*')
#     print('*' * (4 * n - 3))

# n = 3일 때 n = 2일 때 보다 위/아래에 두 줄 더 붙고 양 옆에 별이랑 뛰어쓰기 생김
# print('*' * (4 * n - 3))
# print('*' + ' ' * (4 * n - 3 - 2) + '*')
#위의 두 줄이 다시 사용됨


# 재귀 함수 이용
n = int(input())

def add_star(inside): # 기존 star 모양 양 옆에 별 추가하는 함수
    return '* '+ inside +' *'

def star(n):
    if n ==1:
        return['*']
    else:
        return ['*'*(4*n-3), '*'+' '* (4*n-5)+'*'] + list(map(add_star, star(n-1))) + ['*'+' '* (4*n-5)+'*', '*'*(4*n-3)]

print('\n'.join(star(n)))

    # print('*' * (4 * n - 3))
    # print('*' + ' ' * (4 * n - 3 - 2) + '*')
    # print()


