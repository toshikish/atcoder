N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()

c = {'r': P, 's': R, 'p': S}
ans = 0
for j in range(K):
    for i in range(j, N, K):
        if i == j:
            con = 1
            ans += c[T[i]]
        elif T[i] == T[i - K]:
            con += 1
            if con % 2 == 1:
                ans += c[T[i]]
        else:
            con = 1
            ans += c[T[i]]

print(ans)
