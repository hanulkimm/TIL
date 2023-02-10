import sys

sys.stdin = open('input.txt', 'r')


t = int(input())
for tc in range(t):
    st = input()
    n = len(st)

    print('..#'+'...#'*(n-1)+'..')
    print('.#'*2*n+'.')
    middle = []
    for chr in st:
        middle.append(f'#.{chr}.')
    middle.append('#')
    print(*middle, sep='')
    print('.#' * 2 * n+'.')
    print('..#' + '...#' * (n - 1) + '..')