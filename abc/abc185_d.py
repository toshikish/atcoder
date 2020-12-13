N, M = map(int, input().split())
A = [0] + list(map(int, input().split())) + [N + 1]

if N == M:
    ans = 0
else:
    A.sort()
    B = []
    for i in range(1, M + 2):
        Bi = A[i] - A[i - 1] - 1
        if Bi > 0:
            B.append(Bi)
    m = min(B)
    ans = sum([(Bi + m - 1) // m for Bi in B])
print(ans)
