import sys
sys.stdin = open('input.txt', 'r')

t = int(input())
for tc in range(t):
    n = int(input())
    nums = list(map(int, input()))

    sm = 0
    mx = 0
    diff = 0
    for i in range(n-1):
        if nums[i] == 1:
            for j in range(i+1, n):
                if nums[j] == 0: # 연속이 끊기는 경우
                    sm = j-i
                    break
                if j == n-1: # 끝까지 연속한 경우
                    sm = n-i
            if mx < sm:
                mx = sm
    print(f'#{tc+1} {mx}')






