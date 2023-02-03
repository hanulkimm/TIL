import sys
sys.stdin = open('input.txt', 'r')

t = int(input())
for tc in range(t):
    n = int(input())

    total = []

    for i in range(n):
        num, a, b = map(int, input().split())
        stop = []

        if num == 1:
            for j in range(a, b+1):
                stop.append(j)

        if num == 2:
            stop.append(a)
            stop.append(b)
            if a % 2 == 0: # a 짝수
                for j in range(a+1, b):
                    if j % 2 == 0:
                        stop.append(j)
            else: # a 홀수
                for j in range(a+1, b):
                    if j % 2 != 0:
                        stop.append(j)

        if num == 3:
            stop.append(a)
            stop.append(b)
            if a % 2 == 0:
                for j in range(a+1, b):
                    if j % 4 == 0:
                        stop.append(j)
            else:
                for j in range(a+1, b):
                    if j % 3 == 0 and j % 10 != 0:
                        stop.append(j)

        total.append(stop)

    mx = 0
    for i in range(1001):
        cnt = 0
        for case in total:
            if i in case:
                cnt += 1
        if mx < cnt:
            mx = cnt

    print(f'#{tc+1} {mx}')
