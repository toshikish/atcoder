N = int(input())
a = list(map(int, input().split()))

ans = -10000
for i in range(N):
    max_pa = -10000
    max_pt = -10000
    for j in range(N):
        if i == j:
            continue
        _i, _j = sorted([i, j])
        pt = sum(a[_i:_j+1:2])
        pa = sum(a[_i+1:_j+1:2])
        if pa > max_pa:
            max_pa = pa
            max_pt = pt
    ans = max(ans, max_pt)
print(ans)
