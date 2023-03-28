def turn(lst, num):
    n = len(lst)
    tmp = 0
    for j in range(n - 1, -1, -1):
        if lst[j] == 1:
            tmp += num ** (n - 1 - j)
        if lst[j] == 2:
            tmp += num ** (n - 1 - j) * 2
    if num == 2:
        two_alst.append(tmp)
    if num == 3:
        three_alst.append(tmp)


dct1 = {1: 0, 0: 1}
dct2 = {0: [1, 2], 1: [0, 2], 2: [0, 1]}
t = int(input())
for tc in range(1, t + 1):
    two_lst = list(map(int, input()))
    three_lst = list(map(int, input()))
    two_alst = []
    three_alst = []
    for i in range(len(two_lst)):
        two_lst[i] = dct1[two_lst[i]]
        turn(two_lst, 2)
        two_lst[i] = dct1[two_lst[i]]
    for k in range(len(three_lst)):
        for l in range(2):
            tmp_n = three_lst[k]
            three_lst[k] = dct2[three_lst[k]][l]
            turn(three_lst, 3)
            three_lst[k] = tmp_n
    ans = 0
    for ch in two_alst:
        if ch in three_alst:
            ans = ch
    print(f'#{tc} {ans}')