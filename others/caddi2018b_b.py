N, H, W = map(int, input().split())
P = [tuple(map(int, input().split())) for i in range(N)]

print(len(list(filter(lambda p: p[0] >= H and p[1] >= W, P))))
