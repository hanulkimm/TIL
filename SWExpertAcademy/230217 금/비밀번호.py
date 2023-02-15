import sys
sys.stdin = open('input.txt', 'r')


for tc in range(1, 4):
    n, st = input().split()
    stk = []
    for ch in st:
        if stk:
            if stk[-1] == ch:
                stk.pop()
            else:
                stk.append(ch)
        else:
            stk.append(ch)
    print(f'#{tc} ', *stk, sep='')
