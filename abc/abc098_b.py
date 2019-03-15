N = int(input())
S = input()

ans = 0
for i in range(1, N):
    s1 = set(S[:i])
    s2 = set(S[i:])
    ans = max(ans, len(s1 & s2))

print(ans)
