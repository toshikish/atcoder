N = int(input())
a = list(map(int, input().split()))

n = [1]
for i in range(1, N):
    if a[i - 1] < a[i]:
        n[-1] += 1
    else:
        n.append(1)
ans = N
for ni in n:
    if ni == 1:
        continue
    ans += ni * (ni - 1) // 2
print(ans)
