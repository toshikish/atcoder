K, N = map(int, input().split())
A = list(map(int, input().split()))

A.append(A[0] + K)
D = [A[i + 1] - A[i] for i in range(N)]
print(K - max(D))
