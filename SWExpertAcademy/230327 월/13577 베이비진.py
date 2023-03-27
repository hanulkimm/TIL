import sys
sys.stdin = open('input.txt', 'r')

t = int(input())
for tc in range(1, t+1):
    lst = list(map(int, input()))
    lst.sort()
    dct = {}
    for i in range(10):
        dct[i] = 0
    for n in lst:
        dct[n]+=1

    ans = 0
    for key in dct:
        if dct[key] >= 3:
            ans += 1
            dct[key]-=3
    for n in range(8):
        if dct[n]>=1 and dct[n+1]>=1 and dct[n+2]>=1:
            ans += 1
            dct[n]-=1
            dct[n+1]-=1
            dct[n+2]-=1
    if ans >=2:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')

