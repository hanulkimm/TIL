import sys
sys.stdin = open('input.txt', 'r')

# t = int(input())
# for tc in range(1, t+1):
#     n = int(input())
#     lst = list(map(int, input().split()))
#
#     # 가장 제일 큰 값 찾아주기 -> 최대값에서 이전 값들 빼주고 --> 반복
#     i = ans = 0
#     while i < n:
#         i_mx = i
#         for j in range(i+1, n):
#             if lst[i_mx] < lst[j]:
#                 i_mx = j
#         for j in range(i, i_mx):
#             ans += lst[i_mx] - lst[j]
#
#         i = i_mx + 1
#
#     print(f'#{tc} {ans}')
#################################
t = int(input())
for tc in range(1, t + 1):
    N = int(input())
    lst = list(map(int, input().split()))[::-1]
    ans = 0
    mx = lst[0]
    for n in lst[1:]:
        if mx < n:
            mx = n
        else:
            ans += mx - n

    print(f'#{tc} {ans}')
