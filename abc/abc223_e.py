from itertools import permutations

P = list(map(int, input().split()))

ans = False
for h, w in permutations(P[0:2]):
    if sum((p + h - 1) // h for p in P[2:5]) <= w:
        ans = True
    for nP in permutations(P[2:5]):
        nw = w - (nP[0] + h - 1) // h
        if nw <= 0:
            continue
        if sum((p + nw - 1) // nw for p in nP[1:]) <= h:
            ans = True
print('Yes' if ans else 'No')
