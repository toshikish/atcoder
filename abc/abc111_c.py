from collections import defaultdict

n = int(input())
V = list(map(int, input().split()))
 
def mode(d):
    return sorted(d.items(), key=lambda x: x[1], reverse=True)
 
if len(set(V)) == 1:
    ans = n // 2
else:
    o = defaultdict(int)
    e = defaultdict(int)
    for i in range(n):
        if i % 2 == 0:
            e[V[i]] += 1
        else:
            o[V[i]] += 1
    mode_o = mode(o)
    mode_e = mode(e)
    if mode_o[0][0] != mode_e[0][0]:
        ans = n - mode_o[0][1] - mode_e[0][1]
    else:
        ans = min(n - mode_o[0][1] - mode_e[1][1], n - mode_o[1][1] - mode_e[0][1])
print(ans)
