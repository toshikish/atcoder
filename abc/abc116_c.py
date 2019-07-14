N = int(input())
h = list(map(int, input().split()))

ans = 0
while True:
    state = 0
    for i in range(N):
        if state == 0 and h[i] > 0:
            state += 1
            h[i] -= 1
            ans += 1
        elif state == 1 and h[i] > 0:
            h[i] -= 1
        elif state == 1 and h[i] == 0:
            state = 2
            break
    if state == 0:
        break
print(ans)
