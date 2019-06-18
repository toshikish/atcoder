import bisect

N = int(input())
A = list(map(int, input().split()))
A.sort()

neg = [A[0]]
pos = [A[-1]]
if N >= 3:
    i = bisect.bisect_left(A, 0, lo=1, hi=N - 1)
    neg += A[1:i]
    pos += A[i:N - 1]

M = neg.pop()
Op = []
for i in range(len(pos) - 1):
    p = pos.pop()
    Op.append((M, p))
    M -= p
p = pos.pop()
Op.append((p, M))
M = p - M
for i in range(len(neg)):
    n = neg.pop()
    Op.append((M, n))
    M -= n

print(M)
for O in Op:
    print(O[0], O[1])
