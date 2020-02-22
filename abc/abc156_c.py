N = int(input())
X = list(map(int, input().split()))

ans = 1000000000
for P in range(min(X), max(X) + 1):
    S = sum([(Xi - P) * (Xi - P) for Xi in X])
    ans = min(ans, S)
print(ans)
