A, B, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = min(a) + min(b)
for i in range(M):
    xi, yi, ci = map(int, input().split())
    ans = min(ans, a[xi - 1] + b[yi - 1] - ci)
print(ans)
