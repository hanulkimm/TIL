import sys
sys.stdin = open('input.txt', 'r')

def enq(i):
    global last
    last += 1 # 마지막 정점 추가
    heap[last] = i
    c = last
    p = c // 2 # 부모 정점 있는지 확인하기
    while p and heap[p] > heap[c]: # 부모정점 있고 더 크다면 값 바꾸기
        heap[p], heap[c] = heap[c], heap[p]
        c = p # 자식 정점 재설정
        p = p //2

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    lst = list(map(int, input().split()))
    heap = [0] * (n+1)
    last = 0
    for i in lst:
        enq(i)

    ans = 0 # 마지막 노드의 조상 노드들 값 합
    i = n
    while i:
        ans += heap[i//2]
        i = i//2
    print(f'#{tc} {ans}')