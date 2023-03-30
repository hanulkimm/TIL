def msort(lst):
    global cnt
    if len(lst) <= 1:
        return lst

    m = len(lst)//2
    left = msort(lst[:m])
    right = msort(lst[m:])

    if left[-1] > right[-1]:
        cnt += 1

    ret = []
    l = r = 0
    while l<len(left) and r<len(right):
        if left[l]<right[r]:
            ret.append(left[l])
            l += 1
        else:
            ret.append(right[r])
            r += 1
    ret += left[l:] + right[r:]
    return ret

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    lst = list(map(int, input().split()))
    cnt = 0
    ans = msort(lst)
    print(f'#{tc} {ans[n//2]} {cnt}')