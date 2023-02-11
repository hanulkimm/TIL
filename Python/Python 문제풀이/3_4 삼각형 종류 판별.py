# s_triangle 로 삼각형 각 변 입력받아 어떤 삼각형인지 출력

s_triangle = list(map(int,input().split()))

s_triangle.sort()
print(s_triangle)

a = int(s_triangle[0])
b = int(s_triangle[1])
c = int(s_triangle[2])

if a + b > c:
    if a == b == c:
        print('정삼각형')
    elif a ==b != c or a != b == c:
        print('이등변삼각형')
    elif a*a + b*b == c*c:
        print('직각삼각형')
    else:
        print('삼각형')
else:
    print('삼각형 아님')
    

