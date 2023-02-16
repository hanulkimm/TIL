import sys
sys.stdin = open('input.txt', 'r')
t = int(input())

def f(i, n, sm, key):
    global cnt
    if sm > key: 
        return
    elif sm == key:
        cnt += 1
        return
    elif i == n: # 끝까지 돌렸는데 sm == key가 아닌 경우들
        return
    else:
        # bit[i] = 1
        f(i+1, n, sm+lst[i], key)
        # bit[i] = 0
        f(i+1, n, sm, key)


for tc in range(1, t+1):
    n, k = map(int, input().split())
    lst = list(map(int, input().split()))
    cnt = sm = 0
    # bit = [0] * n # 굳이 bit 필요없음
    f(0, n, sm, k)
    print(f'#{tc} {cnt}')


