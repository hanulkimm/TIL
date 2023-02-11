import sys

sys.stdin = open('input.txt', 'r')

t = int(input())

for test_case in range(t):
    n = int(input())
    arr_1 = []
    arr_2 = []
    for tc in range(n):
        a_x, a_y, b_x, b_y, col = list(map(int, input().split()))
        if a_x > b_x:
            a_x, b_x = b_x, a_x
        if a_y > b_y:
            a_y, b_y = b_y, a_y

        for i in range(a_x, b_x+1):
            for j in range(a_y, b_y+1):
                if col == 1:
                    arr_1.append([i, j])
                else:
                    arr_2.append([i, j])

    cnt = 0
    for cs in arr_1:
        if cs in arr_2:
            cnt += 1
    print(f'#{test_case+1} {cnt}')