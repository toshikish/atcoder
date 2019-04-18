N = int(input())
a = list(map(int, input().split()))

ta = []
S = 0
for ai in a:
    S += ai
    ta.append(S)
ans = 10 ** 16
for i in range(len(ta) - 1):
    ans = min(ans, abs(S - 2 * ta[i]))

print(ans)
