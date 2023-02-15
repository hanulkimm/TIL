import sys

sys.stdin = open('input.txt', 'r')

# 방 (1,2)(3,4)(5,6) ... (399, 400) 묶어서 묶은 방들은 같은 index라고 생각
# index는 1~200
# 지나가는 경우를 세는 cnt만들고 지나는 index마다 += 1


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = []
    for _ in range(n):
        s, e = map(int, input().split())
        if s == e: # 현재 방이 돌아갈 방 위치
            n -= 1
            continue
        else:
            # 1~200 index 찾기
            if s % 2: # 홀수 일 때
                a = s // 2 + 1
            if s % 2 ==0:
                a = s // 2
            if e % 2: # 홀수 일 때
                b = e // 2 + 1
            if e % 2 ==0:
                b = e // 2
            if a > b: # 조심하기!!
                a, b = b, a
            arr.append([a, b])
    print(arr)

