import heapq

N, K = map(int, input().split())
V = list(map(int, input().split()))

lesser = min(N, K)
ans = 0
for A in range(lesser + 1):
    for B in range(lesser + 1):
        if A + B > lesser:
            continue
        holding = V[:A] + V[N - B:]
        heapq.heapify(holding)
        S = sum(holding)
        CD = K - (A + B)
        for i in range(min(A + B, CD)):
            p = heapq.heappop(holding)
            if p >= 0:
                break
            S -= p
        ans = max(ans, S)
print(ans)
