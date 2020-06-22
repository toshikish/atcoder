N, K = map(int, input().split())
A = list(map(int, input().split()))

fin = min(A) == N
for j in range(K):
    if fin:
        break
    T = [0] * (N + 1)
    for i in range(N):
        T[max(i - A[i], 0)] += 1
        T[min(i + A[i] + 1, N)] -= 1
    A[0] = T[0]
    fin = A[0] == N
    for i in range(1, N):
        A[i] = A[i - 1] + T[i]
        if A[i] < N:
            fin = False
print(' '.join(list(map(str, A))))
