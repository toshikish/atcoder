A, B = map(int, input().split())

d = abs(A - B)
T = [0, 1, 2, 3, 2, 1, 2, 3, 3, 2]
print(d // 10 + T[d % 10])
