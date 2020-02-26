T = int(input())
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

ans = False
if N >= M:
    c = 0
    for Bi in B:
        while c < N:
            if A[c] <= Bi <= A[c] + T:
                c += 1
                break
            c += 1
        else:
            break
        continue
    else:
        ans = True

print('yes' if ans else 'no')
