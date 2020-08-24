H, W, M = map(int, input().split())
R = [0] * H
C = [0] * W
B = []
for i in range(M):
    hi, wi = map(lambda s: int(s) - 1, input().split())
    R[hi] += 1
    C[wi] += 1
    B.append((hi, wi))

Rmax = max(R)
Cmax = max(C)
ans = Rmax + Cmax
if R.count(Rmax) * C.count(Cmax) == sum([R[hi] == Rmax and C[wi] == Cmax for hi, wi in B]):
    ans -= 1

print(ans)
