import sys

sys.stdin = open('input.txt', 'r')

t = int(input())

for tc in range(t):
    st, p = input().split()
    n, m = len(st), len(p)

    cnt = 0
    i = 0
    while i < n-m+1:
        if st[i:i+m] == p: # p 가 포함되어있다면
            cnt += 1
            i = i+m # 단어 다음 위치로 이동, 겹치는 경우 제외하기 위함
        else:
            i += 1
    cnt += n - cnt * m # p의 개수 * p의 길이를 전체 길이에서 빼준만큼 더해주기

    print(f'#{tc+1} {cnt}')



