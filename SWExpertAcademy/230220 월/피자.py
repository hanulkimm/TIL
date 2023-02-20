t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    lst= list(map(int, input().split()))
    q = [] # 화덕 개수(크기)
    for i in range(1, n+1):
        q.append((i, lst.pop(0)))
    while q: # 화덕이 빌 때 까지
        num, c = q.pop(0)
        c = c//2
        if c == 0:
            if lst:
                i += 1
                q.append((i, lst.pop(0)))
        else:
            q.append((num, c))
    ans = num
    print(f'#{tc} {ans}')