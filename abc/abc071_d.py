N = int(input())
S1 = input()
S2 = input()
MOD = 1000000007

c = 0
ans = 1
if S1[c] == S2[c]:
    ans *= 3
    c += 1
else:
    ans *= 6
    c += 2
while c < N:
    if S1[c] == S2[c]:
        ans *= 2 if S1[c - 1] == S2[c - 1] else 1
        c += 1
    else:
        ans *= 2 if S1[c - 1] == S2[c - 1] else 3
        c += 2
    ans %= MOD
print(ans)
