from collections import defaultdict
n = int(input())
V = list(map(int, input().split()))

def modification(d):
    d_keys = list(d.values())
    if len(d_keys) == 1:
        return 0
    d_keys.sort(reverse=True)
    return int(n / 2) - d_keys[0]

if len(set(V)) == 1:
    print(int(n / 2))
else:
    o = defaultdict(int)
    e = defaultdict(int)
    for i in range(n):
        if i % 2 == 0:
            e[V[i]] += 1
        else:
            o[V[i]] += 1
    print(modification(o) + modification(e))
