import sys

sys.stdin = open('input.txt', 'r')

t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    mx = 0
    for _ in range(2): # arr 와 전치행렬
        for i in range(n): # 행기준으로
            for j in range(m - 1):  # 최소 길이가 2니까 m-1까지
                if arr[i][j] == 1:
                    lst = [1]
                    for k in range(j + 1, m):
                        if arr[i][k] == 1:
                            lst.append(1)
                        else:
                            break
                    if mx < len(lst):
                        mx = len(lst)
        arr = list(zip(*arr))

    print(f'#{tc} {mx}')