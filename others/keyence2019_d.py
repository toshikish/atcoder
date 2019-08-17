N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
MOD = 10 ** 9 + 7

MN = M * N
A_gt = [0] * MN
B_gt = [0] * MN
ans = 1
for Ai in A:
    if A_gt[Ai - 1] > 0:
        ans = 0
        break
    A_gt[Ai - 1] = 1
for Bi in B:
    if B_gt[Bi - 1] > 0:
        ans = 0
        break
    B_gt[Bi - 1] = 1

if ans != 0:
    for i in range(MN - 2, -1, -1):
        A_gt[i] += A_gt[i + 1]
        B_gt[i] += B_gt[i + 1]
    ans = A_gt[MN - 1] * B_gt[MN - 1]
    for i in range(MN - 2, -1, -1):
        is_max_in_A = A_gt[i] != A_gt[i + 1]
        is_max_in_B = B_gt[i] != B_gt[i + 1]
        if is_max_in_A and is_max_in_B:
            ans *= 1
        elif is_max_in_A:
            ans *= B_gt[i]
        elif is_max_in_B:
            ans *= A_gt[i]
        else:
            ans *= A_gt[i] * B_gt[i] - (MN - 1 - i)
        ans %= MOD
print(ans)
