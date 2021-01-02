N = int(input())
S = [input() for i in range(N)]

A = set()
B = set()
ans = 'satisfiable'
for Si in S:
    if Si[0] == '!':
        w = Si[1:]
        A.add(w)
        if w in B:
            ans = w
            break
    else:
        w = Si
        B.add(w)
        if w in A:
            ans = w
            break
print(ans)
