N, D = map(int, input().split())
walls = []
for _ in range(N):
    Li, Ri = tuple(map(int, input().split()))
    walls.append((Ri, Li))

walls.sort()
t = 0
ans = 0
for i in range(N):
    Ri, Li = walls[i]
    if Li <= t:
        continue
    t = Ri + D - 1
    ans += 1
print(ans)
