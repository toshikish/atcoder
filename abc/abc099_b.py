a, b = map(int, input().split())
print(sum(list(range(1, b - a + 1))) - b)
