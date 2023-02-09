import sys

sys.stdin = open('input.txt', 'r')

for tc in range(10):
    m = int(input())
    arr = [list(input()) for _ in range(8)]

    cnt = 0
    for lst in arr:
        for i in range(8-m+1):
            if lst[i:i+m] == lst[i:i+m][::-1]:
                cnt += 1
    arr2 = list(zip(*arr))
    for lst in arr2:
        for i in range(8-m+1):
            if lst[i:i+m] == lst[i:i+m][::-1]:
                cnt += 1
    print(f'#{tc+1} {cnt}')
