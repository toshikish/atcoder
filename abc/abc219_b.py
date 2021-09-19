S = [input() for _ in range(3)]
T = input()

ans = ''
for ti in T:
    ans += S[int(ti) - 1]
print(ans)
