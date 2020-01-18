H = int(input())
W = int(input())
N = int(input())

u = max(H, W)
print((N + u - 1) // u)
