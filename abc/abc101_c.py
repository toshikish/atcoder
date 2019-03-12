N, K = map(int, input().split())
A = list(map(int, input().split()))

def op(n, k):
    ans = 1 if n % (k - 1) > 0 else 0
    return n // (k - 1) + ans

i = A.index(1)
left = i
right = N - (i + 1)

if N == K:
    ans = 1
elif left <= K - 2 or right <= K - 2:
    ans = 1 + op(N - K, K)
else:
    ans = op(left, K) + op(right, K)
print(ans)
