from collections import defaultdict

N, K = map(int, input().split())
c = list(map(int, input().split()))

cnt = defaultdict(int)
for i in range(K):
    cnt[c[i]] += 1

ans = len(cnt.keys())
t = ans
for i in range(K, N):
    if cnt[c[i]] == 0:
        t += 1
    cnt[c[i]] += 1
    if cnt[c[i - K]] == 1:
        t -= 1
    cnt[c[i - K]] -= 1
    ans = max(ans, t)

print(ans)
