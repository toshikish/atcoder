from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

B = sorted([(A[i], i + 1) for i in range(N)], reverse=True)
dp = defaultdict(int)

for S in range(1, N + 1):
    for x in range(S + 1):
        y = S - x
        candid = []
        if x >= 1:
            candid.append(dp[(x - 1, y)] + B[S - 1][0]
                          * (B[S - 1][1] - x))
        if y >= 1:
            candid.append(dp[(x, y - 1)] + B[S - 1][0]
                          * ((N - y + 1) - B[S - 1][1]))
        dp[(x, y)] = max(candid)

print(max([dp[(i, N - i)] for i in range(N + 1)]))
