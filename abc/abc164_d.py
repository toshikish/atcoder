S = list(map(int, list(input()[::-1])))

N = len(S)
P = 2019
C = [0] * P
B = 1
t = 0
ans = 0
for i in range(N):
    C[t] += 1
    t = (t + S[i] * B) % P
    ans += C[t]
    B = B * 10 % P
print(ans)
