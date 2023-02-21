## 괄호검사 ##
t = int(input())
for tc in range(1, t+1):
    st = input()
    stk = []
    ans = 1
    for ch in st:
        if ch == '(':
            stk.append(ch)
        else:
            if stk:
                stk.pop()
            else:
                ans = 0
                break
    if stk:
        ans = 0
    print(f'#{tc} {ans}')

## 괄호검사 ##
dct = {'(': ')', '{': '}'}
t = int(input())
for tc in range(1, t+1):
    st = input()
    stk = []
    ans = 1
    for ch in st:
        if ch in dct:
            stk.append(dct[ch])
        elif ch == '}' or ch == ')':
            if stk:
                if stk[-1] == ch:
                    stk.pop()
                else:
                    ans = 0
                    break
            else:
                ans = 0
                break
    if stk:
        ans = 0
    print(f'#{tc} {ans}')

## 파스칼의 삼각형 ##
# 양 옆을 0으로 채운 arr 만든 후, 위와 왼쪽 대각선 더해주는 식
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [[0] * (n+1) for _ in range(n+1)]
    arr[1][1] = 1

    for i in range(2, n+1):
        for j in range(1, i+1):
            arr[i][j] = arr[i-1][j] + arr[i-1][j-1]
    print(f'#{tc}')

    for i in range(1, n+1):
        for j in range(1, i+1):
            print(arr[i][j], end= ' ')
        print()

## 반복문자 지우기 ##
t = int(input())
for tc in range(1, t+1):
    st = input()
    stk = []
    for ch in st:
        if stk:
            if stk[-1] == ch:
                stk.pop()
            else:
                stk.append(ch)
        else:
            stk.append(ch)
    ans = len(stk)
    print(f'#{tc} {ans}')

## dfs ##
def dfs_stk(start):
    stk = []  # 돌아올 자리 표시
    v = [0] * (V + 1)  # 방문 표시

    s = start
    v[s] = 1
    ans.append(s)

    while True:
        for e in adj[s]:
            if v[e] == 0:
                stk.append(s)
                s = e
                ans.append(s)
                v[s] = 1
                break
        else: # 모든 경로가 이미 방문했다면
            if stk:
                s = stk.pop()
            else:
                break


t = int(input())
for tc in range(1, t+1):
    V, E = map(int, input().split())
    adj = [[] for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
    for lst in adj:
        lst.sort()

    ans = []
    dfs_stk(1)
    print(f'#{tc}', *ans, sep=' ')

## 그래프 경로 ##
t = int(input())
for tc in range(1, t+1):
    V, E = map(int, input().split())
    adj = [[] for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int, input().split())
        adj[a].append(b)
    s, g = map(int, input().split())
    ans = 0
    stk = []
    v = [0] * (V+1)
    v[s] = 1

    while True:
        for e in adj[s]:
            if v[e] == 0:
                stk.append(s)
                s = e
                v[e] = 1
                break
        else:
            if s == g:
                ans = 1
                break
            else:
                if stk:
                    s = stk.pop()
                else:
                    ans = 0
                    break
    print(f'#{tc} {ans}')

## forth ##
dct = {'+': 1, '*': 2}
t = int(input())
for tc in range(1, t+1):
    lst = list(input().split())
    stk = []
    ans = stk
    for ch in lst:
        if ch == '.':
            ans = stk.pop()
            break
        else:
            if ch in dct:
                if len(stk)>=2 :
                    a = stk.pop()
                    b = stk.pop()
                    if ch == '+':
                        stk.append(a+b)
                    elif ch == '-':
                        stk.append(b-a)
                    elif ch == '*':
                        stk.append(b*a)
                    else:
                        stk.append(int(b/a))
                else:
                    ans = 'error'
                    break
            else:
                stk.append(int(ch))
    if stk:
        ans = 'error'
    print(f'#{tc} {ans}')

## 미로 ##
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr =[list(map(int,input())) for _ in range(n)]
    v = [[0] * n for _ in range(n)]
    print(arr)
    for i in range(n):
        for j in range(n):
            if arr[i][j] ==2:
                si, sj = i, j
            elif arr[i][j] == 3:
                ei, ej = i, j

    stk = []
    ci, cj = si, sj
    v[ci][cj] = 1

    while True:
        for di, dj in ((0, -1), (0, 1), (-1, 0), (1, 0)):  # 좌우상하
            ni, nj = ci + di, cj + dj
            if 0 <= ni < n and 0 <= nj < n and v[ni][nj] == 0 and arr[ni][nj] != 1:
                stk.append((ci, cj))

                ci, cj = ni, nj
                v[ci][cj] = 1
                break

        else:
            if stk:
                ci, cj = stk.pop()
            else:

                break
    ans = v[ei][ej]
    print(f'#{tc} {ans}')

