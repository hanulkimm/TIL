## 노드의 합 ##
t = int(input())
for tc in range(1, t+1):
    n, m, l = map(int, input().split())
    lst = [0] * (n+1)
    for _ in range(m):
        a, b =map(int, input().split())
        lst[a] = b
    for i in range(n,l-1,-1):
        lst[i//2] += lst[i]
    ans = lst[l]
    print(ans)

# 이진탐색 #
def inorder(i):
    global cnt
    if 1<=i<=n:
        inorder(i*2)
        lst[i] = cnt
        cnt += 1
        inorder(i*2+1)

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    lst = [0] * (n+1)
    cnt = 1
    inorder(1)
    print(f'#{tc} {lst[1]} {lst[n//2]}')

# 중위 순회 #
def inorder(i):
    if 1<=i<=n:
        inorder(i*2)
        ans.append(lst[i])
        inorder(i*2+1)

t = 10
for tc in range(1, t+1):
    n = int(input())
    lst = [0] * (n+1)
    for p in range(1, n+1):
        tlst = input().split()
        lst[p] = tlst[1]
    ans = []
    inorder(1)
    print(f'#{tc} ', *ans, sep='')

# 전위순회 #
def preorder(i):
    if i:
        ans.append(i)
        preorder(left[i])
        preorder(right[i])

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    info = list(map(int, input().split()))
    left = [0] * (n+1)
    right = [0] * (n+1)
    for i in range(n-1):
        p, c = info[i*2], info[i*2+1]
        if left[p]==0:
            left[p]=c
        else:
            right[p]=c
    ans = []
    preorder(1)
    print(f'#{tc}', *ans)

# subtree #
def preorder(i):
    if i:
        alst.append(i)
        preorder(left[i])
        preorder(right[i])

t = int(input())
for tc in range(1, t+1):
    e, n = map(int, input().split())
    left = [0] * (e+2)
    right = [0] * (e+2)
    lst = list(map(int, input().split()))
    for i in range(e):
        p, c = lst[i*2], lst[i*2+1]
        if left[p]==0:
            left[p]=c
        else:
            right[p]=c
    alst = []
    preorder(n)
    print(len(alst))
