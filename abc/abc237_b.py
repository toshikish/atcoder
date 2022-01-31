H, W = map(int, input().split())
A = [input().split() for _ in range(H)]

for j in range(W):
    print(' '.join([A[i][j] for i in range(H)]))
