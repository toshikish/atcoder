A = list(map(int, input().split()))
A.sort()

def solve(a, b):
    if (b - a) % 2 == 0:
        return (b - a) // 2
    else:
        return (b - a + 1) // 2 + 1

ans = 0
if (A[2] - A[0]) % 2 == 1 and (A[2] - A[1]) % 2 == 1:
    A[2] -= 1
    ans += 1
ans += solve(A[0], A[2]) + solve(A[1], A[2])
print(ans)
