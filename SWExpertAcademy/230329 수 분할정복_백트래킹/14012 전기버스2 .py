# 백트래킹
def dfs(i, cnt, sm):
    global ans
    if i==n:
        ans = min(ans, cnt)
        return

    # 교체 안 하는 경우
    if sm>0: # 배터리 잔량 있을 때만 가능
        dfs(i+1, cnt, sm-1)
    # 교체하기 ( 모든 정류장 마다 배터리 잔량이 0보다 큼)
    dfs(i+1, cnt+1, lst[i]-1)

t = int(input())
for tc in range(1, t + 1):
    lst = list(map(int, input().split()))
    n = lst[0]
    ans = n
    dfs(2,0,lst[1]-1) # idx, cnt, sm
    print(ans)


# DP
t = int(input())
for tc in range(1, t + 1):
    n, *charge = list(map(int, input().split()))
    dp = [0] * n
    for i in range(n-1):
        for j in range(i+1, i+charge[i]+1): # 갈 수 있는 거리
            if j <=n-1: # 범위 내이고
                if dp[j]==0: # 한번도 안 갔으면
                    dp[j]=dp[i]+1
                elif dp[j]>dp[i]+1: # 이미 간 적이 있고 더 적게 걸리면
                    dp[j] = dp[i]+1
    ans = dp[-1] -1 # 처음 충전한 경우 빼주기
    print(f'#{tc} {ans}')
