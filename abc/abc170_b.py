X, Y = map(int, input().split())
print('Yes' if Y % 2 == 0
      and 2 * X - Y // 2 >= 0 and Y // 2 - X >= 0 else 'No')
