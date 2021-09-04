X, Y = input().split('.')
Y = int(Y)
print(X + '-' if 0 <= Y <= 2 else X if 3 <= Y <= 6 else X + '+')
