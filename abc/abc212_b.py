X = list(map(int, list(input())))
print('Weak' if all(X[i] == X[i + 1] for i in range(3))
      or all(X[i + 1] == (X[i] + 1) % 10 for i in range(3)) else 'Strong')
