N, W = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]

items.sort(reverse=True)
value = 0
weight = W
for Ai, Bi in items:
    w = min(Bi, weight)
    value += Ai * w
    weight -= w
    if weight == 0:
        break
print(value)
