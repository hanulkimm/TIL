import sys
sys.stdin = open('input.txt', 'r')

def babygin(lst):
    cnt  =[0]*10
    for ch in lst:
        cnt[ch] += 1
    tmp = 0
    for num in cnt:
        if num >= 3:
            tmp += 1
            num -= 3
    for i in range(8):
        if cnt[i]>=1 and cnt[i+1]>=1 and cnt[i+2]>=1:
            tmp+=1
            cnt[i]-=1
            cnt[i+1]-=1
            cnt[i+2]-=1
    if tmp>=1:
        return True

t = int(input())
for tc in range(1, t + 1):
    lst = list(map(int, input().split()))
    a_lst = []
    b_lst = []
    for i in range(6):
        a_lst.append(lst[i*2])
        b_lst.append(lst[i*2+1])
    e = 3
    ans = 0
    while e < 7:
        if babygin(a_lst[:e]):
            ans = 1
            break
        if babygin(b_lst[:e]):
            ans = 2
            break
        e += 1
    print(f'#{tc} {ans}')
