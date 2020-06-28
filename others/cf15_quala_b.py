N = int(input())
A = list(map(int, input().split()))

print(sum([A[i] * 2 ** (N - i - 1) for i in range(N)]))
