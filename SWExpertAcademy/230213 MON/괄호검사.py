import sys
sys.stdin = open('input.txt', 'r')

t = int(input())
for tc in range(1, t+1):
    ans = 1
    st = input()
    stk = []
    for ch in st:
        if ch == '(':
            stk.append(ch)
        else:
            if stk:
                stk.pop()
            else:
                ans = 0
                break
    if stk:
        ans = 0
    print(f'#{tc} {ans}')

#     stack = []
#     top = -1
#
#     ans = 1
#     for i in lst:
#         if i == '(':
#             stack.append(i)
#             top += 1
#         if i == ')':
#             if len(stack) == 0:
#                 ans = -1
#                 break
#             else:
#                 stack.pop()
#                 top -= 1
#
#     if len(stack) != 0 or ans == -1:
#         ans = 0
#     print(f'#{tc} {ans}')
# #
#
#