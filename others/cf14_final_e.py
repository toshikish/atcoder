N = int(input())
R = list(map(int, input().split()))

dpu = dpd = 1
for i in range(1, N):
    nu = dpu
    nd = dpd
    if R[i - 1] < R[i]:
        nd = dpu + 1
    if R[i - 1] > R[i]:
        nu = dpd + 1
    dpu = nu
    dpd = nd

M = max(dpu, dpd)
print(M if M >= 3 else 0)
