N, K = map(int, input().split())
L = [tuple(map(int, input().split())) for _ in range(N)]
L.sort()

m = K
i = 0
cur = 0
while m > 0:
    cur += m
    m = 0
    while i < N and L[i][0] <= cur:
        m += L[i][1]
        i += 1
print(cur)
