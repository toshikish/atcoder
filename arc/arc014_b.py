N = int(input())
W = [input() for i in range(N)]

ans = 'DRAW'
used_words = {W[0]}
for i in range(1, N):
    if W[i] in used_words or W[i][0] != W[i - 1][-1]:
        ans = 'WIN' if i % 2 == 1 else 'LOSE'
        break
    used_words.add(W[i])
print(ans)
