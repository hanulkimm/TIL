import sys
sys.stdin = open('input.txt', 'r')

t = int(input())
for tc in range(t):
    n = int(input())
    lst = list(map(int, input().split()))


    mx = 0
    for i in range(n-1):
        sm = 1
        for j in range(i+1, n):

            if lst[j] > lst[j-1]: # 계속해서 연속한 경우
                sm += 1
            else: # 연속하지 않는 순간 loop stop
                break

        if mx < sm:
            mx = sm

    print(f'#{tc + 1} {mx}')










