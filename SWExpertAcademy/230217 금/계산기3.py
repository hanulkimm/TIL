import sys
sys.stdin = open('input.txt', 'r')

dct = {'(':0, '+':1, '*': 2} # stack안에서의 우선순위

t = 10
for tc in range(1, t+1):
    n = int(input())
    st = input()
    stk = []
    alst = [] # 후위 표기식
    for ch in st:
        if ch == '(': # 항상 append
            stk.append(ch)
        elif ch == '+' or ch == '*':
            if stk:
                while True:
                    if dct[stk[-1]] >= dct[ch]:
                        alst.append(stk.pop())
                    else:
                        stk.append(ch)
                        break
            else:
                stk.append(ch)
        elif ch == ')':
            while True:
                if stk[-1] == '(':
                    stk.pop()
                    break
                else:
                    alst.append(stk.pop()) # append 해준 '(' 빼주기
        else:
            alst.append(ch)
    if stk:
        for i in stk[::-1]:
            alst.append(i)

    stk2 = []
    for n in alst:
        if n in dct:
            if stk2:
                a = stk2.pop()
                b = stk2.pop()
                if n == '+':
                    stk2.append(b+a)
                else:
                    stk2.append(b*a)
        else:
            stk2.append(int(n)) # 정수 처리
    print(f'#{tc}', *stk2)