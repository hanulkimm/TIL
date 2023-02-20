import sys
sys.stdin = open('input.txt', 'r')

t = 10
for tc in range(1, t+1):
    _ = int(input())
    q = list(map(int, input().split()))

    i = 1
    while True:
        if i == 1:
            k = q.pop(0)-1
            q.append(k)
        elif i == 2:
            k = q.pop(0)-2
            q.append(k)
        elif i == 3:
            k = q.pop(0)-3
            q.append(k)
        elif i == 4:
            k = q.pop(0)-4
            q.append(k)
        else:
            k = q.pop(0)-5
            q.append(k)
        i = (i + 1) % 5
        if k <= 0:
            break

    q.pop()
    q.append(0)
    print(f'#{tc}', *q)