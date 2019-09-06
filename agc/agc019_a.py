Q, H, S, D = map(int, input().split())
N = int(input())

p1 = min(Q * 4, H * 2, S)
p2 = min(p1 * 2, D)

print(N % 2 * p1 + N // 2 * p2)
