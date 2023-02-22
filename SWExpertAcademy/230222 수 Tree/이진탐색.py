import sys
sys.stdin = open('input.txt', 'r')

def inorder(i):
    if i:
        inorder(left[i])
        alst.append(i)
        inorder(right[i])

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    lst = [0] * (n+1) # 자식 인덱스의 부모노드번호
    for i in range(1, n+1):
        lst[i] = i//2
    left = [0] * (n+1) # 부모 인덱스의 자식 노드 번호
    right = [0] * (n+1)
    for i in range(1, n+1):
        p, c = lst[i], i
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c
    alst = []
    inorder(1)

    for i in range(n):
        if alst[i]==1:
            ans1 = i+1
        if alst[i]==n//2:
            ans2 = i+1
    print(f'#{tc} {ans1} {ans2}')

