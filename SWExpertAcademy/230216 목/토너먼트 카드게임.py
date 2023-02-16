tbl = [0, 2, 3, 1] # a가 지는 숫자들
def solve(s, e):
    if s == e:
        return s
    a = solve(s, (s+e)//2)
    b = solve((s+e)//2+1, e)

    if tbl[lst[a]] == lst[b]:
        return b
    return a

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    lst = [0] + list(map(int, input().split()))
    ans = solve(1, n)
    print(f'#{tc} {ans}')