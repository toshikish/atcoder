A, B, C, D = map(int, input().split())

M = 200
prime = [True] * (M + 1)
for i in range(2, M + 1):
    if not prime[i]:
        continue
    j = 2
    while i * j <= M:
        prime[i * j] = False
        j += 1

x = A + C
t = 0
ans = False
while x <= B + D:
    if prime[x]:
        t = 0
    else:
        t += 1
        if t == D - C + 1:
            ans = True
            break
    x += 1
print('Takahashi' if ans else 'Aoki')
