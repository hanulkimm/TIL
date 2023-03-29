## 시간초과!!!

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    n_lst = list(map(int, input().split()))
    m_lst = list(map(int, input().split()))
    ans = 0
    for ch in m_lst:
        if ch in n_lst: # 우선 n_lst에 존재
            M = ch # 찾는 값
            s, e = 0, n-1
            stk = []
            flag = False
            while s<=e:
                if flag:
                    break
                mid = (s+e)//2
                if n_lst[mid]==M:
                    break
                elif n_lst[mid] > M:
                    e = mid-1
                    if stk:
                        if stk[-1]==1: # 같은 방향이면
                            flag = True
                    stk.append(1)
                else:
                    s = mid + 1
                    if stk:
                        if stk[-1]==2: # 같은 방향이면
                            flag = True
                    stk.append(2)

            if not flag: # 양쪽 구간 번갈아 선택했으면
                ans += 1
    print(f'#{tc} {ans}')