N, A, X, Y = map(int, input().split())
print(X * N if N <= A else X * A + Y * (N - A))
