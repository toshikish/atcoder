N = int(input())
A = list(map(int, input().split()))

B = [False] * 2001
for Ai in A:
    B[Ai] = True

i = 0
while B[i]:
    i += 1
print(i)
