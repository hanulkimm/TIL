# 13869
t = int(input())
for tc in range(t):
    n = int(input())
    lst = list(map(int, input().split()))

    for i in range(n-1,0,-1):
        for j in range(i):
            if lst[j] > lst[j+1]:
                lst[j] , lst[j+1] = lst[j+1], lst[j]

    print(f'#{tc+1}', *lst)


## 13599 View ##
import sys
sys.stdin = open('input.txt', 'r')
# [1] 조망권이 확보되는지 확인해주는 함수 만들기
def check(lst, i):
    if lst[i - 2] < lst[i] and lst[i - 1] < lst[i] and lst[i + 1] < lst[i] and lst[i + 2] < lst[i]:
        return True
# [2] 주변 4개 중 가장 높은 높이 구하는 함수 만들기(elif 아님 주의)
def max_level(i):
    mx = lst[i - 2]
    if mx < lst[i - 1]:
        mx = lst[i - 1]
    if mx < lst[i + 1]:
        mx = lst[i + 1]
    if mx < lst[i + 2]:
        mx = lst[i + 2]
    return mx


for tc in range(3):
    n = int(input())
    lst = list(map(int, input().split()))
    ans = 0

    for i in range(2, n - 2):
        if check(lst, i):
            ans += lst[i] - max_level(i)
    print(f'#{tc + 1} {ans}')

##  함수 안 쓰고 ##
for tc in range(3):
    n = int(input())
    lst = list(map(int, input().split()))
    ans = 0
    m = 2
    for i in range(m, n-m):
        mx = lst[i-m]
        for j in range(i-m+1, i+m+1):
            if i ==j:
                continue
            else:
                if mx < lst[j]:
                    mx = lst[j]
        if lst[i] > mx:
            ans += lst[i] - mx

## 13588 구간합 ##
for tc in range(t):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))

    # [1] for 반복문 사용하기
    mx = 0
    mn = m * 10000
    for i in range(n-m+1):
        sm = 0
        for j in range(m):
            sm += lst[i+j]
        if mx < sm:
            mx = sm
        if mn > sm:
            mn = sm
    print(f'#{tc+1} {mx-mn}')

    # [2] loop 줄이기
    sm = 0
    for i in range(m):
        sm += lst[i]
    mx = mn = sm 
    for j in range(m, n):
        sm += lst[j]
        sm -= lst[j-m]
        if mx < sm:
            mx = sm
        if mn > sm:
            mn = sm
        
## 13576 Gravity ## 
t = int(input())

for tc in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    print(lst)

    ans = 0
    for i in range(n-1):
        sm = n-i-1 # 장애물없이 떨어졌을 경우, 가장 큰 낙차
        for j in range(i+1, n):
            if lst[j] >= lst[i]:
                sm -= 1
        if ans < sm:
            ans = sm
    print(f'# {tc+1} {ans}')

## 13560 min-max ##
t = int(input())

for tc in range(t):
    n = int(input())
    lst = list(map(int, input().split()))

    mx = lst[0]
    mn = lst[0]
    for i in range(1,n):
        if mx < lst[i]:
            mx = lst[i]
        if mn > lst[i]:
            mn = lst[i]
    print(f'{tc+1} {mx-mn}')

## 13869 정렬 연습 ##

t = int(input())
for tc in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    for i in range(n-1, 0, -1):
        for j in range(i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    print(f'#{tc+1}', *lst)

## 13655 Flatten ##
# 최대, 최소 값이 가변적이라는 것을 생각하기
# 최대, 최소 구하는 함수 만들기
def min_max(lst):
    i_mn = i_mx = 0
    for i in range(1, len(lst)):
        if lst[i_mx] < lst[i]:
            i_mx = i
        if lst[i_mn] > lst[i]:
            i_mn = i
    return i_mn, i_mx

for tc in range(10):
    n = int(input()) # 평탄화 횟수
    lst = list(map(int, input().split()))
    for _ in range(n):
        idx_mn, idx_mx = min_max(lst)
        if lst[idx_mx] - lst[idx_mn] <= 1:
            break
        lst[idx_mn] += 1
        lst[idx_mx] -= 1
    
    idx_mn, idx_mx = min_max(lst) # 최종 idx 구해주기
    print(f'{tc+1} {lst[idx_mx]-lst[idx_mn]}')

## 13589 숫자 카드 ##
t = int(input())
for tc in range(t):
    n = int(input())
    lst = list(map(int, input()))
    cnt = [0] * 10

    for i in lst:
        cnt[i] += 1

    mx = 0
    idx = 0
    for i in range(10):
        if mx <= cnt[i]:
            mx = cnt[i]
            idx = i

    print(f'#{tc+1} {idx} {mx}')

## 13577 Baby-Gin ##
t = int(input())
for tc in range(t):
    lst = list(map(int, input()))

    cnt = [0]*10
    for n in lst:
        cnt[n] += 1

    ans = 0
    i = 0
    while i < 10:
        if cnt[i] >= 3:
            ans += 1
            cnt[i] -= 3
        else:
            i += 1
    i = 0
    while i <= 7:
        if cnt[i]>=1 and cnt[i+1] >= 1 and cnt[i+2] >= 1:
            ans += 1
            cnt[i] -= 1
            cnt[i+1] -= 1
            cnt[i+2] -= 1
        else:
            i += 1

    print(f'#{tc+1} {ans//2}')

## 15200 두 개의 숫자열 ##

t = int(input())
for tc in range(10):
    n, m = map(int, input().split())
    a_lst = list(map(int, input().split()))
    b_lst = list(map(int, input().split()))

    if n > m:
        n, m = m, n
        a_lst, b_lst = b_lst, a_lst
    mx = 0
    for j in range(m-n+1):
        sm = 0
        for i in range(n):
            sm += a_lst[i]*b_lst[i+j]
        if mx < sm:
            mx = sm
    print(f'#{tc+1} {mx}')    

## 13998 새로운 버스 노선 ##

t = int(input())
for tc in range(t):
    n = int(input())
    cnt = [0] * 1001 # 0~1000
    for _ in range(n):
        tp, a, b = map(int, input().split())

        if tp == 1:
            for i in range(a, b+1):
                cnt[i] += 1
        if tp == 2:
            cnt[a] += 1
            cnt[b] += 1
            for i in range(a+1,b):
                if a % 2: # 홀수
                    if i % 2: # 홀수
                        cnt[i] += 1
                else:
                    if i % 2 == 0:
                        cnt[i] += 1
        if tp == 3:
            cnt[a] += 1
            cnt[b] += 1
            for i in range(a+1, b):
                if a % 2: # 홀수
                    if i % 3 == 0 and i % 10 != 0 :
                        cnt[i] += 1
                else:  #짝수
                    if i % 4 == 0:
                        cnt[i] += 1
    mx = 0
    for i in cnt:
        if mx < i:
            mx = i
    print(f'#{tc+1} {mx}')

## 13618 삼성시의 버스 노선 ##
t = int(input())
for tc in range(t):
    n = int(input())
    cnt = [0] * 5001 #0~5000
    for _ in range(n):
        a, b = map(int, input().split())
        for i in range(a, b+1):
            cnt[i] += 1
    print(cnt)

    p = int(input())
    lst = [int(input()) for _ in range(p)]
    ans = []
    for i in lst:
        print(cnt[i], end=' ')
        
## 13617 현주의 상자 바꾸기 ##
t = int(input())
for tc in range(t):
    n, q = map(int, input().split())
    cnt = [0]*n
    for i in range(1,q+1):
        l, r = map(int, input().split())
        for j in range(l-1,r):
            cnt[j] = i
    print(f'#{tc+1}',*cnt)

## 13616 간단한 소인수분해 ##
t = int(input())
for tc in range(t):
    n = int(input())
    dct = {2:0,3:0, 5:0, 7:0, 11:0 }
    while n > 1:
        for key in dct:
            if n % key == 0:
                dct[key] += 1
                n = n / key
    ans = []
    for key in dct:
        ans.append(dct[key])
    print(f'#{tc+1}', *ans)

## 9386 연속한 1의 개수 ##
t = int(input())
for tc in range(t):
    n = int(input())
    lst = list(map(int, input()))

    mx = 0
    for i in range(n-1):
        if lst[i] == 1:
            cnt = 1
            for j in range(i+1,n):
                if lst[j] == 1:
                    cnt += 1
                else:
                    break
    if mx < cnt :
        mx = cnt
    print(f'#{tc+1} {mx}')
    
## 9367 점점 커지는 당근의 개수 ##

t = int(input())
for tc in range(t):
    n = int(input())
    lst = list(map(int, input().split()))

    mx = 0
    for i in range(n-1):
        cnt = 1
        for j in range(i+1, n):
            if lst[i] < lst[j]:
                cnt += 1
            else:
                break
        if mx < cnt:
            mx = cnt
    print(f'#{tc+1} {mx}')
