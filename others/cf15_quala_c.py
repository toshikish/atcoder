from bisect import bisect_left

N, T = map(int, input().split())
A = []
B = []
for i in range(N):
    Ai, Bi = map(int, input().split())
    A.append(Ai)
    B.append(Bi)

if sum(B) > T:
    ans = -1
elif sum(A) <= T:
    ans = 0
else:
    D = [A[i] - B[i] for i in range(N)]
    D.sort(reverse=True)
    accD = D[:]
    for i in range(1, N):
        accD[i] = accD[i - 1] + D[i]
    ans = bisect_left(accD, sum(A) - T) + 1
print(ans)
