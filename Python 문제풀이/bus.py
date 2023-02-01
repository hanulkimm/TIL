import sys
sys.stdin = open('bus.txt','r')

tc = int(input())
for _ in range(tc):
    n = int(input())
    path = []
    for i in range(1, n+1):
        ai, bi = map(int, input().split())
        path.append([ai, bi])

    station = []
    p = int(input())
    for j in range(1, p+1):
        cj = int(input())
        station.append(cj)

    rst = {}
    for j in range(p):
        rst[j] = 0
        for i in range(n):
            if station[j] in range(path[i][0], path[i][1]+1):
                rst[j] += 1

    ans = list(rst.values())
    print(f'#{tc}', *ans)


