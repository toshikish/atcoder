N, A, B = map(int, input().split())
print(B * N if N <= 5 else B * 5 + A * (N - 5))
