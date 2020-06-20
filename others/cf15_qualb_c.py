from bisect import bisect_left

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()
i = -1
ans = False
for Bi in B:
    i = bisect_left(A, Bi, i + 1)
    if i == N:
        break
else:
    ans = True
print('YES' if ans else 'NO')
