def judge(L):
    l = len(L)
    if l <= 2:
        return True
    return all(L[i + 1] - L[i] == L[i + 2] - L[i + 1] for i in range(l - 2))


def ltoi(L):
    return int(''.join(list(map(str, L))))


X = list(map(int, list(input())))
if judge(X):
    ans = ltoi(X)
else:
    N = len(X)
    d = d0 = X[1] - X[0]
    needs_count_up = True
    for d in range(d0, 10):
        lsb = X[0] + d * (N - 1)
        if lsb > 9:
            break
        if lsb < 0:
            continue
        ans = ltoi(list(X[0] + d * i for i in range(N)))
        if ans > ltoi(X):
            needs_count_up = False
            break
    if needs_count_up:
        X[0] += 1
        d = X[0] // (N - 1)
        ans = ltoi(list(X[0] - d * i for i in range(N)))

print(ans)
