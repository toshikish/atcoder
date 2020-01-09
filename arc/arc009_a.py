N = int(input())

p = 0
for i in range(N):
    ai, bi = map(int, input().split())
    p += ai * bi
print(int(p * 1.05))
