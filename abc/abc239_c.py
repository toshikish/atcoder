x1, y1, x2, y2 = map(int, input().split())

neighbors = [set() for _ in range(2)]
P = [(x1, y1), (x2, y2)]
for i in range(2):
    x, y = P[i]
    for dx, dy in [(1, 2), (2, 1)]:
        for px in [1, -1]:
            for py in [1, -1]:
                neighbors[i].add((x + px * dx, y + py * dy))

print('Yes' if neighbors[0].intersection(neighbors[1]) else 'No')
