from collections import defaultdict

N = int(input())
S = input()
MOD = 10 ** 9 + 7

counter = defaultdict(int)
for s in S:
    counter[s] += 1

ans = 1
for v in counter.values():
    ans *= v + 1
    ans %= MOD
print(ans - 1)
