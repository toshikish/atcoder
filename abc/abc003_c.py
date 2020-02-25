N, K = map(int, input().split())
R = list(map(int, input().split()))

R.sort(reverse=True)
print(sum([R[i] / (2 ** (i + 1)) for i in range(K)]))
