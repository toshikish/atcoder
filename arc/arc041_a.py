x, y = map(int, input().split())
k = int(input())

print(x + k if k <= y else x + 2 * y - k)
