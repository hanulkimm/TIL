# 이진수 반환하는 함수 만들기

def dec_to_bin(number):

    result = []

    def new_bin(number):
    
        if number == 1:
            result.append(1)
    
        else:
            if number % 2 == 0:
                result.append(0)
                new_bin(number // 2)
            else:
                result.append(1)
                new_bin(number // 2)
    new_bin(number)

    result.reverse()
    return ''.join(map(str,result))

print(dec_to_bin(50)) # 110010