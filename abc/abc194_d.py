N = int(input())
print(sum(N / (N - i) for i in range(1, N)))
