import sys

sys.stdin = open('input.txt', 'r')

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    time_lst = []
    for _ in range(n):
        time_lst.append(list(map(int, input().split())))

    time_lst.sort(key=lambda x: x[0]) # 시작 시간 기준 정렬
    time_lst.sort(key=lambda x: x[1]) # 완료 시간 기준 정렬

    ans = 1 # 첫번째 거 선택
    i = 0
    while True:
        flag = True
        for j in range(i+1,n):
            if time_lst[i][1] <= time_lst[j][0]:
                flag = False
                ans += 1
                i = j
                break
        if flag: # 더 이상 사용할 화물차 없으면
            break
    print(f'#{tc} {ans}')
