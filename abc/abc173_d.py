N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)
print(A[0] + sum(A[1:(N - 2) // 2 + 1]) * 2 + A[(N - 2) // 2 + 1] * (N % 2))
