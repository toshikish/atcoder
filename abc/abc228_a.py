S, T, X = map(int, input().split())

if S < T:
    ans = S <= X < T
else:
    ans = S <= X or X < T
print('Yes' if ans else 'No')
