N, K, S = map(int, input().split())

M = 1000000000
_S = M - 1 if S == M else M
print(' '.join(list(map(str, [S] * K + [_S] * (N - K)))))
