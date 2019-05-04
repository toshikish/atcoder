import math

N = int(input())

def digits(A):
    ans = 1
    while A >= 10:
        A //= 10
        ans += 1
    return ans

def F(A, B):
    return max(digits(A), digits(B))

ans = 11
for A in range(1, int(math.sqrt(N)) + 1):
    B = N // A
    if A * B == N:
        ans = min(ans, F(A, B))
print(ans)
