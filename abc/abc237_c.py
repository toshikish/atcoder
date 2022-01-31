S = input()

N = len(S)
n1 = 0
while n1 < N:
    if S[n1] != 'a':
        break
    n1 += 1
n2 = 0
while n2 < N:
    if S[N - 1 - n2] != 'a':
        break
    n2 += 1

if n1 > n2:
    ans = False
elif n1 == n2 == N:
    ans = True
else:
    T = S[n1:N - n2]
    M = len(T)
    ans = True
    for i in range(M // 2 + 1):
        if T[i] != T[M - 1 - i]:
            ans = False
            break

print('Yes' if ans else 'No')
