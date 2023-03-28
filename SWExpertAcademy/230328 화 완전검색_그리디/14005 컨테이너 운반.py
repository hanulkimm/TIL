import sys
sys.stdin = open('input.txt', 'r')

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split()) # 컨테이너 수, 트럭 수
    w = list(map(int, input().split()))
    t = list(map(int, input().split()))
    ans = 0
    w.sort(reverse=True)
    t.sort(reverse=True)
    for i in range(m):
        for j in range(n):
            if t[i]>=w[j] and w[j]!=0:
                ans += w[j]
                w[j]=0
                break
    print(f'#{tc} {ans}')