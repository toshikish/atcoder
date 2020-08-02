N, D = map(int, input().split())
P = [tuple(map(int, input().split())) for i in range(N)]

print(sum([p * p + q * q <= D * D for p, q in P]))
