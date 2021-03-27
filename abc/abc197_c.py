from functools import reduce

N = int(input())
A = list(map(int, input().split()))

ans = 1 << 64
for bit in range(1 << (N - 1)):
    B = []
    b = A[0]
    for i in range(1, N):
        if bit >> (i - 1) & 1:
            B.append(b)
            b = A[i]
        else:
            b |= A[i]
    B.append(b)
    ans = min(ans, reduce(lambda x, y: x ^ y, B))
print(ans)
