A, op, B = input().split()
A, B = map(int, (A, B))
print(A + B if op == '+' else A - B)
