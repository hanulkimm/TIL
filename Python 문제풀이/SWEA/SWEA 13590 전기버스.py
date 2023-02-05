import sys
sys.stdin = open('input.txt','r')


t = int(input())
for tc in range(t):
    k, n, m = map(int, input().split())
    lst = list(map(int, input().split()))

    cnt = 0  # 충전횟수
    start = 0
    for j in range(n - k):

        for i in range(k, 0, -1):  # 갈 수 있는 정류장 중 가장 먼 것 부터
            if start + i in lst:
                start = start + i
                cnt += 1
                break
            if start >= n - k:
                break
    if start < n - k:  # 종점 도달 못 한 경우
        cnt = 0

    print(f'#{tc + 1} {cnt}')