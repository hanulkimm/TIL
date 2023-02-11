import sys

sys.stdin = open('input.txt', 'r')

t = int(input())

for tc in range(t):
    a_lst = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    dict = {"ZRO":0, "ONE":0, "TWO":0, "THR":0, "FOR":0, "FIV":0, "SIX":0, "SVN":0, "EGT":0, "NIN":0}
    a, b = input().split()
    print(a)
    b = int(b)
    b_lst = input().split()
    for wrd in b_lst:
        dict[wrd] += 1

    ans = []
    for wrd in a_lst:
        for i in range(dict[wrd]):
            ans.append(wrd)
    print(*ans)



    # ans = []
    # for key, value in dict.items():
    #     for i in range(value):
    #         ans.append(key)
    # print(*ans)
