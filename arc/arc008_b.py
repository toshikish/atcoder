from collections import Counter

N, M = map(int, input().split())
name = input()
kit = input()

cn = Counter(name)
ck = Counter(kit)

if set(cn.keys()) <= set(ck.keys()):
    ans = max([(cn[s] + ck[s] - 1) // ck[s] for s in name])
else:
    ans = -1
print(ans)
