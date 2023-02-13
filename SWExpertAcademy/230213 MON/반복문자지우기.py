import sys
sys.stdin = open('input.txt', 'r')

t = int(input())
for tc in range(1, t+1):
    st = input()
    stk = []
    for i in st:
        if stk:
            if i != stk[-1]:
                stk.append(i)
            else:
                stk.pop()
        else:
            stk.append(i)
    print(f'#{tc} {len(stk)}')