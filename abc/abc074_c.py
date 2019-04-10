A, B, C, D, E, F = map(int, input().split())

W = set()
for a in range(F // (100 * A) + 1):
    for b in range(F // (100 * B) + 1):
        if a == b == 0: continue
        w = 100 * (A * a + B * b)
        if w <= F:
            W.add(w)

S = set()
for c in range(F // C + 1):
    for d in range(F // D + 1):
        s = C * c + D * d
        if s <= F:
            S.add(s)

max_density = -1
max_ws = 0
max_s = 0
for w in W:
    for s in S:
        if w + s > F or E * w / 100 < s: continue
        density = s / (w + s)
        if density > max_density:
            max_density = density
            max_ws = w + s
            max_s = s

print(max_ws, max_s)
