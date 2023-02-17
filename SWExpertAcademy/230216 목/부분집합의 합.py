import sys
sys.stdin = open('input.txt', 'r')

def dfs(i, sm, cnt):
    global ans
    if i == N:
        if sm == K and cnt == CNT:
            ans += 1
        return
    dfs(i+1, sm + lst[i], cnt +1)
    dfs(i+1, sm, cnt)

t = int(input())
for tc in range(1, t+1):
    CNT, K = map(int, input().split())
    lst = [i for i in range(1, 13)]
    N = 12
    ans = 0
    dfs(0, 0, 0)
    print(f'#{tc} {ans}')


# def f(i, n, m, sm, key):
#     global ans
#     if i == n: # 끝까지 돌리고
#         if sm == key: # 합이 key이고
#             cnt = 0
#             for j in range(n):
#                 if bit[j]:
#                     cnt += 1
#             if cnt == m: # 부분집합 원소의 개수가 m일 때
#                 ans += 1
#     else:
#         bit[i] = 1
#         f(i+1, n, m, sm+lst[i], key)
#         bit[i] = 0
#         f(i+1, n, m, sm, key)


# t = int(input())
# for tc in range(1, t+1):
#     m, k = map(int, input().split()) # m 부분집합 수, k 부분집합 원소들 합
#     lst = [i for i in range(1, 13)]
#     n = 12 # 집합의 원소의 개수
#     bit = [0] * 12
#     ans = sm = 0
#     f(0, n, m, sm, k)
#     print(f'#{tc} {ans}')

