n = int(input())

def fn_d(n):
    return n + sum(list(int(i) for i in str(n)))

print(fn_d(n))
    
def is_selfnumber(n):
    return len([i for i in range(n) if fn_d(i) == n]) == 0 # self- number 면 true

print(is_selfnumber(n))



