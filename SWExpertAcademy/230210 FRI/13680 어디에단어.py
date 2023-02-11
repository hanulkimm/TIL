import sys

sys.stdin = open('input.txt', 'r')

t = int(input())
for tc in range(t):
    n, k = map(int, input().split())

    # [1] 단어 퍼즐을 0 으로 한 줄 감싸기(왜냐? 길이가 딱 맞아야 되기 때문에)
    arr = [[0] * (n+2)] + [[0]+ list(map(int, input().split()))+[0] for _ in range(n)] + [[0] * (n+2)]

    match = [1] * k # 자릿수 맞는 경우

    cnt = 0
    for lst in arr:
        for i in range(1, n-k+2):
            if lst[i] == 1:
                if lst[i-1] == 0 and lst[i:i+k] == match and lst[i+k]==0:
                    cnt += 1


    arr2 = list(zip(*arr)) # 전치행렬 사용
    for tpl in arr2:
        for i in range(1, n-k+2):
            if tpl[i] == 1:
                if tpl[i-1] == 0 and list(tpl[i:i+k]) == match and tpl[i+k]==0: # zip했을 때 tuple이니까 다시 list 로 만들어주기
                    cnt += 1

    print(f'#{tc+1} {cnt}')