import sys
sys.stdin = open('input.txt', 'r')

def inorder(i):
    if i:
        inorder(left[i])
        alst.append((word[i]))
        inorder(right[i])

t= 10
for tc in range(1, t+1):
    n = int(input())
    left = [0] * (n+1)
    right = [0] * (n + 1)
    word = [[] for _ in range(n+1)]
    for _ in range(n):
        lst = input().split()
        if len(lst)==4:
            p, w, l, r = lst
            p, l, r = int(p), int(l), int(r)
            word[p] = w
            left[p] = l
            right[p] = r
        elif len(lst)==3:
            p, w, l = lst
            p, l = int(p), int(l)
            word[p] = w
            left[p] = l
        else:
            p, w = lst
            p = int(p)
            word[p] = w
    alst = []
    inorder(1)
    print(f'#{tc} ', *alst, sep='')