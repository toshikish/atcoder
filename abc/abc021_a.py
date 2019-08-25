N = int(input())

B = [8, 4, 2, 1]
K = 0
ans = []
for b in B:
    if N >= b:
        ans.append(b)
        N -= b
        K += 1
print(K)
for a in ans:
    print(a)
