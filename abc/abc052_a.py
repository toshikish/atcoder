A, B, C, D = map(int, input().split())
S1, S2 = A * B, C * D
print(S1 if S1 >= S2 else S2)
