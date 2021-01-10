X, Y = map(int, input().split())
X, Y = sorted([X, Y])
print('Yes' if X + 3 > Y else 'No')
