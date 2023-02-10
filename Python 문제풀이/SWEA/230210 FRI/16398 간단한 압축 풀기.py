import sys

sys.stdin = open('input.txt', 'r')

t = int(input())
for tc in range(t):
    print(f'#{tc+1}')
    n = int(input())
    total_lst = [] # 압축 풀었을 때를 한 줄로 표현
    total_cnt = 0
    for _ in range(n):
        ci, ki = input().split()
        for i in range(int(ki)):
            total_lst.append(ci)
            total_cnt += 1

    n_10 = total_cnt // 10 # 너비가 10인 줄의 개수
    n_last = total_cnt % 10 # 마지막 줄의 개수
    for i in range(n_10):
        print(*total_lst[10*i:10*i+10],sep='')
    print(*total_lst[total_cnt-n_last:total_cnt],sep='')


