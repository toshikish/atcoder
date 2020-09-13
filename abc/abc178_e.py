N = int(input())
P = [tuple(map(int, input().split())) for i in range(N)]

X = [x + y for x, y in P]
Y = [x - y for x, y in P]
print(max(max(X) - min(X), max(Y) - min(Y)))
