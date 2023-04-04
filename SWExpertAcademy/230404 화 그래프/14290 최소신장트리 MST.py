import sys
sys.stdin = open('input.txt', 'r')

def find_set(x):
    while x!= rep[x]:
        x = rep[x]
    return x
def union(x,y):
    rep[find_set(y)] = find_set(x)

t = int(input())
for tc in range(1, t+1):
    V, E = map(int, input().split())
    arr = []
    for _ in range(E):
        arr.append(list(map(int, input().split())))
    arr.sort(key=lambda x:x[2]) # 가중치 오름차순 정리
    rep = [ i for i in range(V+1)]
    ans = 0
    cnt = 0
    for s,e,num in arr:
        if find_set(s) != find_set(e): # 미연결
            ans += num # 가중치 더하기
            cnt += 1
            union(s,e)
            if cnt == V:
                break
    print(f'#{tc} {ans}')