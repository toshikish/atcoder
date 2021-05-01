N, D, H = map(int, input().split())
P = [tuple(map(int, input().split())) for _ in range(N)]

print(max([H - D * (H - hi) / (D - di) for di, hi in P] + [0]))
