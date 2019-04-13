A, B = map(int, input().split())
if A < B: A, B = B, A
print(A + B if A - B <= 1 else A + A - 1)
