N = int(input())
a = list(map(int, input().split()))

S = []
n = 0
for ai in a:
    if S:
        if S[-1][0] == ai:
            if S[-1][1] + 1 == ai:
                S.pop()
                n -= ai - 1
            else:
                Si = (ai, S[-1][1] + 1)
                S.pop()
                S.append(Si)
                n += 1
        else:
            S.append((ai, 1))
            n += 1
    else:
        S.append((ai, 1))
        n += 1
    print(n)
