import sys
sys.stdin = open('input.txt', 'r')

def dfs(n, sm):
    global ans
    if ans<=sm:
        return

    if n == N:
        if ans > sm:
            ans = sm
        return
    for j in range(N):
        if v[j] == 0:
            v[j] = 1
            dfs(n+1, sm)
            v[j] = 0

t = int(input())
for tc in range(1, t+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    ans = 10 * N
    v = [0] * N
    dfs(0, 0)


# def pm(i, N): # 열의 순열 구해주기
#     global col
#     if i == N:
#         tmp = []
#         for j in range(len(p)):
#             tmp.append(p[j])
#         col.append(tmp)
#
#     else:
#         for j in range(i, N):
#             p[i], p[j] = p[j], p[i]
#             pm(i+1, N)
#             p[i], p[j] = p[j], p[i]

# t = int(input())
# for tc in range(1, t+1):
#     n = int(input())
#     arr = [list(map(int, input().split())) for _ in range(n)]
#     ans = 0
#     col = []
#     p = [i for i in range(n)]
#     pm(0, n)
#     print(col)
#     mn= 10*n
#     for lst in col:
#         sm = 0
#         for i in range(n):
#             sm += arr[i][lst[i]]
#         if mn > sm:
#             mn = sm
#     print(f'#{tc} {mn}')
#



