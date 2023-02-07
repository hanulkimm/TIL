import sys

sys.stdin = open('input.txt', 'r')

t = int(input())

def binarySearch(lst, n, key):
    st = 0
    end = n-1
    cnt = 1
    while st < end:
        median = (st+end)//2
        if lst[median] == key:
            return cnt
        elif lst[median] < key:
            st = median + 1
            cnt += 1
        else:
            end = median -1
            cnt += 1
    return cnt


for tc in range(t):
    p, a, b = map(int, input().split())
    st = 0
    end = p-1
    cnt_a = 1
    lst = list(range(1, p+1))
    while st < end:
        median = (st + end) // 2
        if lst[median] == a:
            st = 0
            end = p-1
            break
        elif lst[median] < a:
            st = median + 1
            cnt_a += 1
        else:
            end = median - 1
            cnt_a += 1

    cnt_b = 1
    while st < end:
        median = (st + end) // 2
        if lst[median] == b:
            break
        elif lst[median] < b:
            st = median + 1
            cnt_b += 1
        else:
            end = median - 1
            cnt_b += 1

    print(cnt_a, cnt_b)

    if cnt_a < cnt_b:
        print('A')
    elif cnt_a > cnt_b:
        print('B')
    else:
        print(0)


