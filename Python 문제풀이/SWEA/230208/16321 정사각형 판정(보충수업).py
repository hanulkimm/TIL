import sys

sys.stdin = open('input.txt', 'r')

t = int(input())
for tc in range(t):
    n = int(input())
    arr = [list(input()) for _ in range(n)]

    # [1] 가장 오른쪽 끝 꼭짓점 찾기
    for i in range(n):
        for j in range(n):
            if arr[i][j] == '#':
                ei, ej = i, j

    # [2] 정사각형 한 변의 길이 구하기(연속한 길이만)
    sm = 0
    for k in range(ej-1, -1, -1):
        if arr[ei][k] == '#' and arr[ei][k+1] =='#':
            sm += 1
        else:
            break

    cnt = 0
    for i in range(ei, ej-sm-1, -1):
        for j in range(ej, ej-sm-1, -1):
            if arr[i][j] == '#':
                cnt += 1

    total_cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == '#':
                total_cnt += 1


    if cnt == (sm+1)**2 and sm != 0 and cnt == total_cnt:
        print(f'#{tc+1} yes')
    elif total_cnt == 1:  # '#'가 하나 존재하는 경우
        print(f'#{tc + 1} yes')
    else:
        print(f'#{tc+1} no')

