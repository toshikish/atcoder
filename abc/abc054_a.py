A, B = map(int, input().split())

a = 14 if A == 1 else A
b = 14 if B == 1 else B
print('Alice' if a > b else 'Bob' if a < b else 'Draw')
