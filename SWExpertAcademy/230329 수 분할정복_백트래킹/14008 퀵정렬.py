def qsort(lst):
    if len(lst)<=1:
        return lst
    p = lst.pop()
    left = []
    right = []
    for ch in lst:
        if ch < p:
            left.append(ch)
        else:
            right.append(ch)
    return qsort(left) + [p] + qsort(right)


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    lst = list(map(int, input().split()))
    a_lst = qsort(lst)
    ans = a_lst[n//2]
    print(f'#{tc} {ans}')