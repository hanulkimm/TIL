import sys
sys.stdin = open('input.txt', 'r')

t = int(input())
for tc in range(1, t+1):
    print(f'#{tc}')
    n = int(input())
    ans = []
    for i in range(n):
        lst = []
        if i == 0:
            lst.append(1)
        elif i == 1:
            lst.append(1)
            lst.append(1)
        else:
            for j in range(i+1):
                if j == 0 or j == i:
                    lst.append(1)
                else:
                    lst.append(ans[i-1][j]+ans[i-1][j-1])
        ans.append(lst)
    for lst in ans:
        print(*lst)

