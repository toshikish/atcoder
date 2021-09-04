from collections import Counter

N, K = map(int, input().split())
A = list(map(int, input().split()))

C = Counter(A)
B = sorted(C.keys(), reverse=True) + [0]
n = 0
ans = 0
for i in range(len(B) - 1):
    n += C[B[i]]
    k = (B[i] - B[i + 1]) * n
    if K >= k:
        ans += (B[i] - B[i + 1]) * (B[i] + B[i + 1] + 1) // 2 * n
        K -= k
        if K > 0:
            continue
    else:
        q = K // n
        r = K % n
        ans += q * (B[i] * 2 - q + 1) // 2 * n + (B[i] - q) * r
    break

print(ans)
