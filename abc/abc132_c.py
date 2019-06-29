N = int(input())
d = list(map(int, input().split()))

d.sort()
half_N = N // 2
print(d[half_N] - d[half_N - 1])
