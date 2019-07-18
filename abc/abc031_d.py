from collections import defaultdict

K, N = map(int, input().split())
dictionary = [tuple(input().split()) for i in range(N)]

for c in range(3 ** K):
    ls = defaultdict(lambda: 1)
    i = 1
    while c > 1:
        ls[i] = c % 3 + 1
        c //= 3
        i += 1
    ls[i] = c + 1

    ct = {}
    matched = True
    for vi, wi in dictionary:
        left = 0
        for d in vi:
            _d = int(d)
            right = left + ls[_d]
            if _d not in ct:
                ct[_d] = wi[left:right]
            else:
                if ct[_d] != wi[left:right]:
                    matched = False
                    break
            left = right
        if left != len(wi):
            matched = False
    if matched:
        break

for i in range(1, K + 1):
    print(ct[i])
