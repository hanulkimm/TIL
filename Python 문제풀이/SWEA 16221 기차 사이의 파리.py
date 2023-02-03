'''
거 = 속 * 시
250마일/시속 25= 10 시간
그렇다면 파리가 움직인 거리는? 파리의 속력  * 시간
'''

import sys
sys.stdin = open('input.txt', 'r')

t = int(input())
for tc in range(t):
    d, a, b, f = map(int, input().split())
    time = d/(a+b)
    ans = time * f

    print(f'#{tc+1} {ans}')