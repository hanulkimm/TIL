import sys

sys.stdin = open('input.txt', 'r')

t = int(input())

for tc in range(t):
    n, m = map(int, input().split())

    arr = [input() for _ in range(n)]

    # [1] 행 기준으로  회문이 있을 경우
    for lst in arr:
        for i in range(0, n - m + 1):
            cnt = 0
            for j in range(m // 2): # 반을 기준으로 똑같은 단어인지 확인
                if lst[i + j] == lst[i + m - 1 - j]:
                    cnt += 1
            if cnt == m // 2:
                print(f'#{tc+1} {lst[i:i + m]}')

    # [2] 열 기준으로 회문이 있을 경우
    ans = []
    for k in range(n): # 열 고정
        for i in range(0, n - m + 1): # 행 고정
            cnt = 0
            for j in range(m // 2): # 개수
                if arr[i+j][k] == arr[i+m-1-j][k]:
                    cnt += 1
            if cnt == m//2:
                for l in range(m):
                    ans.append(arr[i+l][k])
    if ans != []:
        print(f'#{tc+1} ', *ans, sep='')






