import bisect

N = int(input())
L = list(map(int, input().split()))
L.sort()
ans = 0

for i in range(1, N - 1):
    for j in range(i + 1, N):
        k = bisect.bisect_left(L, L[j] - L[i] + 1, 0, i)
        ans += i - k
print(ans)
