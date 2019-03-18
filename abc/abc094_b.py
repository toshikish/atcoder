N, M, X = map(int, input().split())
A = list(map(int, input().split()))

print(min(len(list(filter(lambda a: a < X, A))), len(list(filter(lambda a: a >= X, A)))))
