from bisect import bisect_left

N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
for _ in range(Q):
    xj = int(input())
    print(N - bisect_left(A, xj))
