from bisect import bisect_left

N, M = map(int, input().split())
H = list(map(int, input().split()))
W = list(map(int, input().split()))

if N == 1:
    ans = min([abs(w - H[0]) for w in W])
else:
    H.sort()
    o = [H[1] - H[0]]
    for i in range(2, N - 2, 2):
        d = H[i + 1] - H[i]
        o.append(o[-1] + d)
    e = [H[2] - H[1]]
    for i in range(3, N - 1, 2):
        d = H[i + 1] - H[i]
        e.append(e[-1] + d)

    ans = 1_000_000_007
    for w in W:
        i = bisect_left(H, w)
        if i <= 1:
            a = abs(H[0] - w) + e[-1]
        elif i >= N - 1:
            a = o[-1] + abs(w - H[N - 1])
        elif i % 2 == 0:
            a = o[(i - 2) // 2] + H[i] - w + e[-1] - e[(i - 2) // 2]
        else:
            a = o[(i - 3) // 2] + w - H[i - 1] + e[-1] - e[(i - 3) // 2]
        ans = min(a, ans)

print(ans)
