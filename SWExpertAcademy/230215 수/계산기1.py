import sys
sys.stdin = open('input.txt', 'r')

t = 10
for tc in range(1, t+1):
    n = int(input())
    st = input()
    stk = []
    ans = []

    # [1] 후위 표기식으로 변환
    for ch in st:
        if ch == '+': # 연산자 일 때
            if stk:
                ans.append(stk.pop())
                stk.append(ch)
            else:
                stk.append(ch)
        else: # 숫자 일 때
            ans.append(ch)
    for ch in stk:
        ans.append(ch)

    # [2] 계산
    stk2 =[]

    for ch in ans:
        if ch == '+':
            a = stk2.pop()
            b = stk2.pop()
            stk2.append(a+b)
        else:
            stk2.append(int(ch))
    print(f'#{tc}', *stk2)

