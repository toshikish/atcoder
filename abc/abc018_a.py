A = int(input())
B = int(input())
C = int(input())

S = sorted([A, B, C], reverse=True)

print(S.index(A) + 1)
print(S.index(B) + 1)
print(S.index(C) + 1)
