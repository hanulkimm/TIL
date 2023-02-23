import sys
sys.stdin = open('input.txt', 'r')

def post(i):
    while i:
        if lst[i//2]==0: # 부모노드가 비어있다면
            lst[i // 2] += lst[i]
            if i % 2: #홀수
                if lst[i-1]:
                    lst[i//2] += lst[i - 1]
            else: # 짝수
                if i < n: # 마지막 수 아닐 떄
                    if lst[i+1]:
                        lst[i//2] += lst[i+1]
        i -= 1

t = int(input())
for tc in range(1, t+1):
    n, m, l = map(int, input().split())
    lst = [0] * (n+1)
    for _ in range(m):
        c, num = map(int, input().split())
        lst[c] = num
    post(n)
    print(f'#{tc} {lst[l]}')

