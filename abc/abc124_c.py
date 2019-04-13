S = input()
N = len(S)

t1 = t2 = 0
for i in range(N):
    c = str(i % 2)
    if S[i] != c:
        t1 += 1
    else:
        t2 += 1
print(min(t1, t2))
