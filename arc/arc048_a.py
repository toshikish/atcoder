A, B = map(int, input().split())
print(B - A if A * B > 0 else B - A - 1)
