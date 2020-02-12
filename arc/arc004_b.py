N = int(input())
d = [int(input()) for i in range(N)]

S = sum(d)
M = max(d)
print(S)
print(max(0, 2 * M - S))
