import sys

sys.stdin = open('input.txt', 'r')

t = int(input())

def binarySearch(lst, n, key):
    start = 1
    ed = n
    cnt = 1
    while start < ed:
        middle = int((start + ed) / 2)
        if middle == key:
            return cnt
        elif middle < key:
            start = middle
            cnt += 1
        else:
            ed = middle
            cnt += 1
    return cnt


for tc in range(t):
    p, a, b = map(int, input().split())
    lst = list(range(1, p+1))
    cnt_a = binarySearch(lst, p, a)
    cnt_b = binarySearch(lst, p, b)

    if cnt_a < cnt_b:
        print(f'#{tc+1} A')
    elif cnt_a > cnt_b:
        print(f'#{tc+1} B')
    else:
        print(f'#{tc+1} 0')


