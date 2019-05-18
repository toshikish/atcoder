H, W = map(int, input().split())
C = [input() for i in range(H)]

for i in range(2 * H):
    print(C[i // 2])
