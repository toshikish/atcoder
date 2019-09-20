x, y = map(int, input().split())

candidates = []
for i in range(1 << 2):
    _x, _y = x, y
    c = 0
    if i & 1:
        _x *= -1
        c += 1
    if i & 2:
        _y *= -1
        c += 1
    if _x <= _y:
        c += _y - _x
        candidates.append(c)
print(min(candidates))
