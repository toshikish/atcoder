a, b, c = map(int, input().split())
print('Yes' if 4 * a * b < (c - a - b) * (c - a - b)
      and c - a - b > 0 else 'No')
