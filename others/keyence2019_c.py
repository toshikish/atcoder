import heapq

N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

if sum(a) < sum(b):
    ans = -1
else:
    ans = 0
    res = 0
    rep = []
    for i in range(N):
        diff = b[i] - a[i]
        if diff > 0:
            ans += 1
            res += diff
        elif diff < 0:
            heapq.heappush(rep, diff)
    while res > 0:
        ans += 1
        res += heapq.heappop(rep)
print(ans)
