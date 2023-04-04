import sys
sys.stdin = open('input.txt', 'r')

def sm_node():
    mn = INF
    idx = 0
    for i in range(n):
        if d[i] < mn and v[i] == 0:
            mn = d[i]
            idx = i
    return idx

def dijkstra(st):
    v[st] = 1
    d[st] = 0
    for way in graph[st]:
        d[way[0]] = way[1]
    for _ in range(n - 1):  # 위에서 첫번째 노드 해줌
        new = sm_node()
        v[new] = 1  # 방문 표시

        for way2 in graph[new]:
            if d[way2[0]] > d[new] + way2[1]:  # 갱신
                d[way2[0]] = d[new] + way2[1]

t = int(input())
for tc in range(1, t + 1):
    INF = 100 * 1000
    n, E = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(E):
        s, e, d = map(int, input().split())
        graph[s].append((e, d))
    v = [0] * n
    d = [INF] * n

    dijkstra(0)
    print(f'#{tc} {d[n - 1]}')
