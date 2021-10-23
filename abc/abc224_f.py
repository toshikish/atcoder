S = list(map(int, list(input())))[::-1]
MOD = 998244353

N = len(S)
B = [1]
T = [1]
for _ in range(N - 1):
    B.append(B[-1] * 2 % MOD)
    T.append(T[-1] * 10 % MOD)

ans = S[0] * B[N - 1]
c = 0
for i in range(1, N):
    c = (c * 10 + B[i - 1]) % MOD
    ans += S[i] * (c + T[i]) * B[N - i - 1]
    ans %= MOD
print(ans)
