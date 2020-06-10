a, b = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

ans = [
    list('x x x x'),
    list(' x x x'),
    list('  x x'),
    list('   x')
]
P = {
    1: (3, 3),
    2: (2, 2),
    3: (2, 4),
    4: (1, 1),
    5: (1, 3),
    6: (1, 5),
    7: (0, 0),
    8: (0, 2),
    9: (0, 4),
    0: (0, 6)
}
for pi in p:
    pos = P[pi]
    ans[pos[0]][pos[1]] = '.'
for qi in q:
    pos = P[qi]
    ans[pos[0]][pos[1]] = 'o'

for l in ans:
    print(''.join(l))
