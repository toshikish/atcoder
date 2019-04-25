x, y = map(int, input().split())
G = {1: 1, 2: 3, 3: 1, 4: 2, 5: 1, 6: 2, 7: 1, 8: 1, 9: 2, 10: 1, 11: 2, 12: 1}
print('Yes' if G[x] == G[y] else 'No')
