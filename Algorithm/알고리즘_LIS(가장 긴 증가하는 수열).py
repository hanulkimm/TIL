# 백준 11053
# 6
# 10 20 10 30 20 50

n = int(input())
lst = list(map(int, input().split()))
dp = [1] * n # 가장 긴 증가하는 수열의 초기 값 = 1
for i in range(1, n):
    for j in range(i): 
        if lst[j] < lst[i]: # 증가하는 경우
            dp[i] = max(dp[i], dp[j]+1) 