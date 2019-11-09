from collections import Counter

N = int(input())
D = list(map(int, input().split()))

c = Counter(D)
ans = 0
if D[0] == 0 and c[0] == 1:
    ans = 1
    M = max(D)
    for i in range(1, M + 1):
        if c[i] == 0:
            ans = 0
            break
        ans *= c[i - 1] ** c[i]
        ans %= 998244353
print(ans)
