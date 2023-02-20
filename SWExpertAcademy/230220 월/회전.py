import sys
sys.stdin = open('input.txt', 'r')

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    queue = list(map(int, input().split()))
    i = 0
    while i < m:
        queue.append(queue.pop(0))
        i += 1
    ans = queue[0]
    print(f'#{tc} {ans}')