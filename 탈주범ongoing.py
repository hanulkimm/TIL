import sys
sys.stdin = open('input.txt', 'r')
## 시작하는 방향에 따라 답이 다르게 나옴
t = int(input())
for tc in range(1, t+1):
    n, m, si, sj, l = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    # [1] 초기 설정
    v = [[0]*m for _ in range(n)] # 방문표시
    stk = [] # 돌아올 자리 표시
    dct = {0:'0', 1: ['u', 'd', 'l', 'r'], 2:['u','d'], 3:['l','r'], 4:['u','r'], 5:['d','r'],6:['d','l'],7:['u','l']}
    di = {'u':-1,'d':1,'l':0,'r':0}
    dj = {'u':0,'d':0,'l':-1,'r':1}
    ops = {'u':'d', 'd':'u', 'l':'r','r':'l'}

    v[si][sj] = 1
    cnt = 1
    ci, cj = si, sj
    while True:
        flag = True
        for dr in dct[arr[ci][cj]]:
            ni, nj = ci+di[dr], cj+dj[dr]
            if 0<=ni<n and 0<=nj<m and v[ni][nj]==0 and (ops[dr] in dct[arr[ni][nj]]) and cnt < l: # 범위내, 미방문, 연결되어 있음
                flag = False
                stk.append([ci,cj])
                ci, cj = ni, nj
                cnt += 1
                v[ci][cj] = 1
                break
        if flag:
            if stk:
                ci, cj = stk.pop()
                cnt -= 1
            else:
                break
    ans = 0
    for lst in v:
        for i in lst:
            if i ==1:
                ans += 1
    print(f'#{tc} {ans}')