import sys
sys.stdin = open('input.txt', 'r')

t = int(input())
for tc in range(1, t+1):
    st = input()
    stk = []
    ans = 1
    top = -1

    dct = {'(': ')', '{': '}'}
    for ch in st:
        if ch in dct:
            stk.append(dct[ch])
        elif ch in dct.values():
            if stk:
                if ch == stk.pop():
                    pass
                else:
                    ans = 0
                    break
            else:
                ans = 0
                break
    print(stk)

    # for ch in st:
    #     if ch == '(' or ch == '{':
    #         stk.append(ch)
    #         top += 1
    #     if ch == ')':
    #         if stk[top] == '(':
    #             top -= 1
    #             stk.pop()
    #         else:
    #             ans = 0
    #             break
    #     if ch == '}':
    #         if stk[top] == '{':
    #             top -= 1
    #             stk.pop()
    #         else:
    #             ans = 0
    #             break
    # if stk:
    #     ans = 0
    #
    # print(f'#{tc} {ans}')
