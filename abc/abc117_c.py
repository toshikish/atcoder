N, M = list(map(int, input().rstrip().split()))
X = list(map(int, input().rstrip().split()))
if N >= M:
    cnt = 0;
elif N == 1:
    cnt = max(X) - min(X)
else:
    X.sort()
    D = []
    for i in range(1, len(X)):
        D.append(X[i] - X[i - 1])
    D.sort()
    del D[-(N - 1):]
    cnt = sum(D)
print(cnt)
