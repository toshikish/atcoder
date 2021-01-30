N, S, D = map(int, input().split())
L = [tuple(map(int, input().split())) for i in range(N)]

ans = any([Xi < S and Yi > D for Xi, Yi in L])
print('Yes' if ans else 'No')
