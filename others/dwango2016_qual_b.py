N = int(input())
K = list(map(int, input().split()))

L = [K[0]] + [min(K[i], K[i + 1]) for i in range(N - 2)] + [K[-1]]
print(' '.join(list(map(str, L))))
