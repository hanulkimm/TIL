import sys
sys.stdin = open('input.txt', 'r')

t = int(input())
for tc in range(1, t+1):
    st = input().split()

    stk = []
    for ch in st:
        if ch == '+':
            if len(stk) >= 2:
                a = stk.pop()
                b = stk.pop()
                stk.append(b + a)
            else:
                ans = 'error'
                break
        elif ch == '-':
            if len(stk) >= 2:
                a = stk.pop()
                b = stk.pop()
                stk.append(b - a)
            else:
                ans = 'error'
                break
        elif ch == '*':
            if len(stk) >= 2:
                a = stk.pop()
                b = stk.pop()
                stk.append(b * a)
            else:
                ans = 'error'
                break
        elif ch == '/':
            if len(stk) >= 2:
                a = stk.pop()
                b = stk.pop()
                stk.append(int(b / a))
            else:
                ans = 'error'
                break
        elif ch == '%':
            if len(stk) >= 2:
                a = stk.pop()
                b = stk.pop()
                stk.append(int(b % a))
            else:
                ans = 'error'
                break
        elif ch == '.':
            if len(stk)>1: # 숫자 1개 이상이면 오류!
                ans = 'error'
                break
            else:
                ans = list(map(int, stk))
                break
        else:
            ch = int(ch)
            stk.append(ch)

    print(f'#{tc} ' , *ans, sep = '')
