'''
444345
102034
667767
'''
import sys

sys.stdin = open('input.txt', 'r')

t = int(input())
for tc in range(t):
    cnt = [0] * 10
    n = list(map(int, input()))
    for x in n:
        cnt[x] += 1

    rn = 0
    triplet = 0
    for i in range(10):
        if cnt[i] >= 3:
            triplet += 1
            cnt[i] -= 3
    for i in range(8):
        if cnt[i] == cnt[i + 1] == cnt[i + 2] == 1:
            rn += 1
            cnt[i] -= 1
            cnt[i + 1] -= 1
            cnt[i + 2] -= 1

    if triplet + rn == 2:
        print(f'#{tc + 1} 1')
    else:
        print(f'#{tc + 1} 0')
