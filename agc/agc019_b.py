A = input()

N = len(A)
h = N // 2
p = 0
for i in range(h):
    if A[i] == A[N - i - 1]:
        p += 1
if p == h:
    ans = 25 * p * 2
elif p == h - 1:
    ans = 24 * 2 + 25 * (h - 1) * 2
    if N % 2 == 1:
        ans += 25
else:
    ans = 25 * h * 2
    if N % 2 == 1:
        ans += 25
print(ans)
