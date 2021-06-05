N, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

threashold = K * K // 2 + 1
low = -1
high = 1_000_000_000
while low + 1 < high:
    mid = (low + high) // 2
    B = [[1 if A[i][j] > mid else 0 for j in range(N)] for i in range(N)]

    S = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(N):
        for j in range(N):
            S[i + 1][j + 1] = B[i][j] + S[i + 1][j] + S[i][j + 1] - S[i][j]

    ok = False
    for i in range(N - K + 1):
        for j in range(N - K + 1):
            t = S[i + K][j + K] - S[i][j + K] - S[i + K][j] + S[i][j]
            if t < threashold:
                ok = True
                break
        else:
            continue
        break

    if ok:
        high = mid
    else:
        low = mid
print(high)
