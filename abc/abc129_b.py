N = int(input())
W = list(map(int, input().split()))

S_left = []
S_right = []
l = r = 0
for i in range(N - 1):
    l += W[i]
    S_left.append(l)
    r += W[N - 1 - i]
    S_right.insert(0, r)

ans = 10 ** 6
for i in range(N - 1):
    ans = min(ans, abs(S_left[i] - S_right[i]))
print(ans)
