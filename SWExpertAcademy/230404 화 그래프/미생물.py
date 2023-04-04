import sys
sys.stdin = open('input.txt', 'r')

di = [0,-1,1,0,0] # 상하좌우
dj = [0,0,0,-1,1]

dct = {1:2, 2:1, 3:4, 4:3}
t = int(input())
for tc in range(1, t + 1):
    n, m, k = map(int, input().split()) # 셀 개수, 격리 시간, 군집 개수
    arr = [list(map(int, input().split())) for _ in range(m)]

    for _ in range(m):
        for i in range(len(arr)):
            arr[i][0] = arr[i][0] + di[arr[i][3]]
            arr[i][1] = arr[i][1] + dj[arr[i][3]]

            if arr[i][0]==0 or arr[i][0]==n-1 or arr[i][1]==0 or arr[i][1]==1:
                arr[i][2] //= 2
                arr[i][3] = dct[arr[i][3]]

        arr.sort(key=lambda x:(x[0], x[1], x[2]), reverse=True)

        i = 1
        while i < len(arr):
            if arr[i-1][:2] == arr[i][:2]:
                arr[i-1][2] += arr[i][2]
            else:
                i += 1
    ans = 0
    for lst in arr:
        ans += lst[2]
    print(f'#{tc} {ans}')