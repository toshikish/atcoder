S = int(input())
MOD = 1_000_000_007

t = [0, 0, 1]
f = 0 if S <= 2 else 1
for i in range(S - 3):
    f = t[0] + 1
    f %= MOD
    t = t[1:3] + [(t[2] + f) % MOD]
print(f)
