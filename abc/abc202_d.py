A, B, K = map(int, input().split())


def f(x, y):
    if x > y:
        x, y = y, x
    c = 1
    for i in range(x):
        c *= (x + y - i)
        c //= (i + 1)
    return c


ans = []
for _ in range(A + B):
    if A == 0:
        ans.append('b')
        continue
    if B == 0:
        ans.append('a')
        continue

    n = f(A - 1, B)
    if K > n:
        ans.append('b')
        B -= 1
        K -= n
    else:
        ans.append('a')
        A -= 1

print(''.join(ans))
