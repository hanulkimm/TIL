import sys

sys.stdin = open('input.txt','rt', encoding='UTF8')

for _ in range(10):
    tc = int(input())
    p = input() # 찾을 문자열
    st = input() # 검색할 문자열

    m = len(p)
    n = len(st)
    cnt = 0
    for i in range(n-m+1):
        if st[i:i+m] == p:
            cnt += 1
    print(f'#{tc} {cnt}')




