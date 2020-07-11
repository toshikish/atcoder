L, R, d = map(int, input().split())
print(R // d - L // d + (1 if L % d == 0 else 0))
