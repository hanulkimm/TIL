import sys

sys.stdin = open('input.txt', 'r')

t = int(input())
for tc in range(t):
    lst = list(map(int, input().split()))
    ans = 0

    for bit in range(1, 1 << 10): # 공집합을 제외한 모든 조합을 bit로 표현
        sm = 0
        for j in range(10): # bit의 0의 자리부터 n-1자리 까지 flag
            if bit & (1 << j):
                sm += lst[j]

        if sm == 0:
            ans = 1
            break
    print(f'#{tc+1} {ans}')