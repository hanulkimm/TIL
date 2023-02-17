import sys
sys.stdin = open('input.txt', 'r')

t = int(input())
for tc in range(1, t+1):
    lst = list(map(int, input())) # 원래 상태
    n = len(lst)

    st_s =[0 for _ in range(n)] # 초기화 상태

    cnt = 0
    for i in range(n):
        if lst[i] == st_s[i]:
            pass
        else:
            cnt += 1
            for j in range(i,n):
                st_s[j] = lst[i]

    print(f'#{tc} {cnt}')
