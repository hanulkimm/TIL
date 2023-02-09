import sys

sys.stdin = open('input.txt', 'r')

t = int(input())

for tc in range(t):
    ans = []
    st = list(input())
    for i in range(len(st)-1,-1,-1):
        if st[i] == 'b':
            ans.append('d')
        elif st[i] == 'd':
            ans.append('b')
        elif st[i] == 'p':
            ans.append('q')
        elif st[i] == 'q':
            ans.append('p')

    print(f'#{tc+1} ', *ans, sep='')

'''
Dictionary 사용하기
dct = {'b':'d', 'd':'b', 'p':'q', 'q':'p'}

t = int(input())

for tc in range(t):
    st = input()[::-1]
    ans = []
    for ch in st:
        alst.append(dct[ch])


'''