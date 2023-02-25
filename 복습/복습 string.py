## 어디에 단어가 들어갈 수 있을까 ##
def count(arr):
    ans = 0
    for lst in arr:
        cnt = 0
        for i in lst:
            if i == 1:
                cnt += 1
            else:
                if cnt == k:
                    ans += 1
                cnt = 0
    return ans
t = int(input())
for tc in range(1, t+1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) + [0] for _ in range(n) ] + [[0] * n]
    arr_t = list(zip(*arr))
    ans = count(arr) + count(arr_t)


    print(f'#{tc} {ans}')


## 간단한 압축 풀기 ##
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    st = ''
    for _ in range(n):
        ch, cnt = input().split()
        st += ch * int(cnt)
    print(f'#{tc}')
    for i in range(0,len(st),10):
        print(st[i:i+10])
        
## 회문 ##
t = int(input())
for tc in range(1,t+1):
    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]

    for _ in range(2):
        for lst in arr:
            for i in range(n-m+1):
                if lst[i:i+m] == lst[i:i+m][::-1]:
                    print(f'#{tc} ', *lst[i:i+m], sep='')
                    break
        arr = list(zip(*arr))
## 회문1 ##
for tc in range(1, 11):
    m = int(input())
    n = 8
    arr = [list(input()) for _ in range(n)]

    ans = 0
    for _ in range(2):
        for lst in arr:
            for i in range(n-m+1):
                if lst[i:i+m] == lst[i:i+m][::-1]:
                    ans += 1
        arr = list(zip(*arr))
    print(f'#{tc} {ans}')


## 회문 2 ##
def isPar(arr, m):
    for lst in arr:
        for i in range(n-m+1):
            if lst[i:i+m] == lst[i:i+m][::-1]:
                return True
    return False


for tc in range(1, 11):
    _ = int(input())
    n = 100
    arr = [list(input()) for _ in range(n)]
    arr_t = list(zip(*arr))

    for m in range(n, 0, -1):
        if isPar(arr, m) or isPar(arr_t,m):
            break
    print(f'#{tc} {m}')


## 문자열의 거울상 ##
t = int(input())
for tc in range(1, t+1):
    lst = list(input())
    dct = {'b': 'd', 'd': 'b', 'p': 'q', 'q': 'p'}
    ans = []
    for key in dct:
        for char in lst:
            if char == key:
                ans.append(dct[key])
    ans = ans[::-1]
    print(f'#{tc} ', *lst, sep = '')


## GNS ##
t = int(input())
for tc in range(1, t+1):
    _, n = input().split()
    lst = list(input().split())
    dct = {"ZRO": 0, "ONE": 0, "TWO": 0, "THR": 0, "FOR": 0, "FIV": 0, "SIX": 0, "SVN": 0, "EGT": 0, "NIN": 0}
    # tbl = "ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"
    # dct = { tbl[n] : 0 for n in range(len(tbl))}

    for char in lst:
        for key in dct:
            if char == key:
                dct[key] += 1
    ans = []
    for key in dct:
        for i in range(dct[key]):
            ans.append(key)

    print(f'#{tc}', *ans)

## 가장 빠른 문자열 타이핑 ##
t = int(input())
for tc in range(1, t+1):
    a, b = input().split()
    n, m = len(a), len(b)

    cnt = 0
    i = 0
    while i < n:
        if a[i:i+m] == b:
            cnt += 1
            i = i+m
        else:
            cnt += 1
            i += 1
    print(f'#{tc} {cnt}')

## 글자수 ##
t = int(input())
for tc in range(1, t+1):
    st1 = list(input())
    st2 = list(input())
    dct = {n:0 for n in set(st1)}

    for key in dct:
        for i in st2:
            if key == i:
                dct[key] += 1

    ans = 0
    for key in dct:
        if ans < dct[key]:
            ans = dct[key]
    print(f'#{tc} {ans}')
