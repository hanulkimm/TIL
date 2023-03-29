def dfs(num, cnt, plus, minus, multiply, divide):
    global mx, mn
    if cnt == n:
        if mx < num:
            mx = num
        if mn > num:
            mn = num
    else:
        if plus:
            dfs(num+lst[cnt], cnt+1, plus-1, minus, multiply,divide)
        if minus:
            dfs(num-lst[cnt], cnt+1, plus, minus-1, multiply, divide)
        if multiply:
            dfs(num * lst[cnt], cnt + 1, plus, minus, multiply-1, divide)
        if divide:
            dfs(int(num / lst[cnt]), cnt + 1, plus, minus, multiply, divide-1)


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    a,b,c,d = list(map(int, input().split()))
    lst = list(map(int, input().split()))
    mn = 1e9
    mx = -1e9
    dfs(lst[0],1,a,b,c,d) # 계산하는 수, 연산자 개수, 더하기, 빼기, 곱하기, 나누기
    ans = mx-mn
    print(f'#{tc} {ans}')