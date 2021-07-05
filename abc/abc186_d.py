from itertools import accumulate

N = int(input())
A = list(map(int, input().split()))

A.sort()
S = list(accumulate(A))
print(sum(S[N - 1] - S[i] - (N - i - 1) * A[i] for i in range(N - 1)))
