# 후위 표기--> 계산
import sys
sys.stdin = open('input.txt', 'r')

def post(i):
    if i:
        post(left[i])
        post(right[i])
        alst.append(lst[i])

t = 10
for tc in range(1, t+1):
    n = int(input()) # 정점의 수
    lst = [0] * (n+1)
    left = [0] * (n+1)
    right = [0] * (n+1)
    for _ in range(n):
        i = input().split()
        if len(i)==4:
            p, ch, l, r = i
            p, l, r = int(p), int(l), int(r)
            left[p] = l
            right[p] = r
        if len(i)==2:
            p, ch = i
            p = int(p)
        lst[p] = ch

    alst = []
    post(1)
    stk = []
    for ch in alst:
        if ch in ('+', '-', '*', '/'):
            a = stk.pop()
            b = stk.pop()
            if ch == '+':
                stk.append(b+a)
            elif ch == '-':
                stk.append(b-a)
            elif ch == '*':
                stk.append(b*a)
            else:
                stk.append(b/a)
        else:
            stk.append(int(ch))
    for i in stk:
        ans = int(i)
    print(f'#{tc} {ans}')

