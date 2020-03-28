X = int(input())

m = X // 500
n = (X % 500) // 5
print(1000 * m + 5 * n)
