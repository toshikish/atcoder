N = int(input())
a = [int(input()) for i in range(N)]

pushed = [False] * N
ans = 0
current = 0
while True:
    ans += 1
    current = a[current] - 1
    if pushed[current]:
        ans = -1
        break
    if current == 1:
        break
    pushed[current] = True
print(ans)
