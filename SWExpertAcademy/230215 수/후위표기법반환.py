import sys
sys.stdin = open('input.txt', 'r')

dct = {'+': 1, '*': 2}
t = int(input())
for tc in range(1, t+1):
    st = input()
    alst = []
    stk = []
    for ch in st:
        if ch == '*' or ch == '+':
            while True:
                if stk:
                    if dct[stk[-1]] >= dct[ch]:
                        alst.append(stk.pop())
                    else:
                        stk.append(ch)
                        break
                else:
                    stk.append(ch)
                    break
        else:
            alst.append(ch)
    for ch in stk[::-1]:
        alst.append(ch)

    print(f'#{tc} ', *alst, sep='')


    
# t = int(input())
# for tc in range(1, t+1):
#     st = input()
#     alst = []
#     stk = []
#     for ch in st:
#         if ch == '*':
#             while True:
#                 if stk:
#                     if stk[-1] == '*':
#                         alst.append(stk.pop())
#                     else:
#                         stk.append(ch)
#                         break
#                 else:
#                     stk.append(ch)
#                     break
#         elif ch == '+':
#             while True:
#                 if stk:
#                     if stk[-1] == '+' or stk[-1] == '*':
#                         alst.append(stk.pop())
#                     else:
#                         stk.append(ch)
#                         break
#                 else:
#                     stk.append(ch)
#                     break
#         else:
#             alst.append(ch)
#     for ch in stk[::-1]:
#         alst.append(ch)
#
#     print(f'#{tc} ', *alst, sep='')