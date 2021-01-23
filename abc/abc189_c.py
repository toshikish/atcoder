N = int(input())
A = list(map(int, input().split()))

ans = 0
done = [0] * N
for i in range(N):
    x = A[i]
    if done[i] == x:
        continue
    l = r = i
    while l >= 0:
        if A[l] < x:
            break
        done[l] = max(x, done[l])
        l -= 1
    l += 1
    while r < N:
        if A[r] < x:
            break
        done[r] = max(x, done[r])
        r += 1
    r -= 1
    ans = max(x * (r - l + 1), ans)

print(ans)
