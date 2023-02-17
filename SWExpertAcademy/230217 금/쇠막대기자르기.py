## 그림 그려보기 ##
t = int(input())
for tc in range(1, t+1):
    st = input()
    n = len(st)
    cnt = 0
    ans = 0
    for i in range(n):
        if st[i] == '(':
            cnt += 1
        else:
            if st[i-1] == '(':
                cnt -= 1
                ans += cnt
            else:
                cnt -= 1
                ans += 1
    print(f'#{tc} {ans}')
