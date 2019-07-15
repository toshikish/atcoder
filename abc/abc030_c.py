N, M = map(int, input().split())
X, Y = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

i = j = 0
t = 0
ans = 0
while t <= a[-1]:
    while i < N:
        if a[i] >= t:
            t = a[i] + X
            i += 1
            break
        i += 1
    while j < M:
        if b[j] >= t:
            t = b[j] + Y
            j += 1
            ans += 1
            break
        j += 1
print(ans)
