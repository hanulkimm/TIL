import sys

sys.stdin = open('input.txt', 'r')

def selectionSort(lst, n):
    for i in range(n-1): # 최대 10개 숫자만 출력
        idx = i
        for j in range(i+1, n):
            if i % 2 == 0: # i가 홀수 일 때
                if lst[idx] < lst[j]: # 최대
                    idx = j
            else:
                if lst[idx] > lst[j]: # 최소
                    idx = j
        lst[i], lst[idx] = lst[idx], lst[i]
    return lst[:10]

t = int(input())

for tc in range(t):
    n = int(input())
    lst = list(map(int, input().split()))

    ans = selectionSort(lst,n)
    print(f'#{tc+1}', *ans)

