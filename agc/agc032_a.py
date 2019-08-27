N = int(input())
b = list(map(int, input().split()))

ans = []
for i in range(N, 0, -1):
    for j in range(i, 0, -1):
        if b[j - 1] == j:
            ans.append(b.pop(j - 1))
            break
    else:
        break
    continue

if len(ans) < N:
    print(-1)
else:
    for i in range(N):
        print(ans[N - 1 - i])
