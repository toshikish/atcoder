N, A, B = map(int, input().rstrip().split())
maximum = min(A, B)
minimum = max(A + B - N, 0)
print(maximum, minimum)
