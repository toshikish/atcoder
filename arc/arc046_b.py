N = int(input())
A, B = map(int, input().split())

f = True
if N <= A:
    f = True
else:
    if A == B:
        f = N % (A + 1) != 0
    else:
        f = A > B
print('Takahashi' if f else 'Aoki')
