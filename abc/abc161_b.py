N, M = map(int, input().split())
A = list(map(int, input().split()))

S = sum(A)
A.sort(reverse=True)
print('Yes' if A[M - 1] >= S / (4 * M) else 'No')
