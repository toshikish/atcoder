from bisect import bisect_right

N, Q = map(int, input().split())
A = [0] + list(map(int, input().split()))

S = [0] * (N + 1)
for i in range(N):
    S[i + 1] = S[i] + A[i + 1] - A[i] - 1

for i in range(Q):
    Ki = int(input())
    p = bisect_right(S, Ki - 1) - 1
    print(A[p] + Ki - S[p])
