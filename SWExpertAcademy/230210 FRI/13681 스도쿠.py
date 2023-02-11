import sys

sys.stdin = open('input.txt', 'r')

t = int(input())

for tc in range(t):
    arr = [list(map(int, input().split())) for _ in range(9)] # 9*9 크기
    arr2 = list(zip(*arr)) # 전치행렬

    ans = 1 # 겹치는 숫자 없으면 1
    for lst in arr: # 행 기준
        for i in range(8):
            if lst[i] in lst[i+1:]:
                ans = 0
    for lst in arr2: # 열 기준
        for i in range(8):
            if lst[i] in lst[i+1:]:
                ans = 0

    loc = [0, 3, 6] # 3X3 작은 격자 기준점들
    nums = [1,2,3,4,5,6,7,8,9]

    for i in loc:
        for j in loc:
            dct = {nums[i]: 0 for i in range(9)}
            for k in range(3):
                for l in range(3):
                    if dct[arr[i+k][j+l]] == 0:
                        dct[arr[i + k][j + l]] += 1
                    else:
                        ans = 0
    print(f'#{tc+1 } {ans}')

