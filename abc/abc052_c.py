from collections import defaultdict

N = int(input())

power = defaultdict(int)
for k in range(2, N + 1):
    _k = k
    for p in range(2, k + 1):
        while _k % p == 0:
            power[p] += 1
            _k //= p
ans = 1
for n in power.values():
    ans *= n + 1
print(ans % (10 ** 9 + 7))
