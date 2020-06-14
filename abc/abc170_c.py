X, N = map(int, input().split())
p = set(map(int, input().split()))

d = 0
while True:
    for sgn in [-1, 1]:
        x = X + sgn * d
        if x not in p:
            break
    else:
        d += 1
        continue
    break
print(x)
