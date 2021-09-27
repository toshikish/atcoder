A, B, C = map(int, input().split())
X = C * ((A + C - 1) // C)
print(X if X <= B else -1)
