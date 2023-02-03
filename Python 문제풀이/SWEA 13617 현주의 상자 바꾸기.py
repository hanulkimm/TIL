import sys
sys.stdin = open('input.txt', 'r')

'''
1
5 2 # n, q # 다음 q개의 줄
1 3 # Li 
2 4 # Ri

0 0 0 0 0
1 1 1
'''
t = int(input())

for tc in range(t):

    n, q = map(int, input().split())
    cnt = [0] * n

    for i in range(1, q+1): # 작업 횟수(1부터 시작)
        l, r = map(int, input().split())

        for j in range(l-1, r):
            cnt[j] = i
    print(f'#{tc+1}', *cnt)



