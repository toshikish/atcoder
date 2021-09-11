N = int(input())
P = list(map(lambda s: int(s) - 1, input().split()))

Q = ['0'] * N
for i in range(N):
    Q[P[i]] = str(i + 1)

print(' '.join(Q))
