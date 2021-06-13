N = int(input())
T = list(map(int, input().split()))

dp = set([0])
for Ti in T:
    ndp = dp.copy()
    for s in dp:
        ndp.add(s + Ti)
    dp = ndp

S = sum(T)
print(min([max(s, S - s) for s in dp]))
