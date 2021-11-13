d, f = map(int, input().split('.'))
print(d + (1 if f // 100 >= 5 else 0))
