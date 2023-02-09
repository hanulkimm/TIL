import sys

sys.stdin = open('input.txt', 'r')

t = int(input())

for tc in range(t):
    str1 = input()
    str2 = list(input())
    n = len(str1)
    m = len(str2)

    tbl = list(set(str1)) # str1에 포함된 글자들
    new_n = len(tbl)
    dct = {tbl[i]: 0 for i in range(new_n)} # str2의 글자들 개수 세기 위한 dictionary

    for char in tbl:
        for i in str2:
            if char == i:
                dct[char] += 1
    ans = 0
    for char in tbl:
        if ans < dct[char]:
            ans = dct[char]
    print(f'#{tc+1} {ans}')

