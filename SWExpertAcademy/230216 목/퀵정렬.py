def qsort(lst):
    if len(lst) <=1: # 더 이상 정렬할 필요 없어짐
        return lst

    p = lst.pop() # 맨 마지막을 pivot으로 설정
    left = []
    right = []
    for i in lst:
        if i < p:
            left.append(i)
        else:
            right.append(i)
    return qsort(left) + [p] + qsort(right)

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    lst = list(map(int, input().split()))
    alst = qsort(lst)
    ans = alst[n//2]
    print(f'#{tc} {ans}')
