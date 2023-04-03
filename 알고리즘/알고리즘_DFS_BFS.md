# 그래프 탐색

## DFS 깊이 우선 탐색
- 시작 정점의 한 방향으로 갈 수 있는 경로가 있는 곳까지 깊이 탐색해 가다가 더 이상 갈 수 없게 되면, 가장 마지막에 만났던 갈림길 간선이 있는 정점으로 되돌아와서 다른 방향의 정점으로 탐색을 계속 반복하여 결국 모든 정점을 방문하는 순회 방법
1.  재귀 사용
```python
def dfs(i):
    v[i]=1
    print(i, end=' ')
    for j in adj[i]:
        if v[j]==0:
            dfs(j)
```
2. 후입선출의 스택 사용
```python
def dfs_stk(start):
    v = [0] * (V+1)
    stk = []

    s = start
    v[s] = 1
    alst.append(s)

    while True:
         for e in adj[s]:
             if v[e] == 0:
                 stk.append(s)
                 s = e
                 v[s] = 1
                 alst.append(s)
                 break
         else:
            if stk:
                s = stk.pop()
            else:
                break
```

## BFS 너비 우선 탐색