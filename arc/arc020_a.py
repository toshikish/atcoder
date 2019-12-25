A, B = map(int, input().split())
a, b = abs(A), abs(B)
print('Ant' if a < b else 'Bug' if a > b else 'Draw')
