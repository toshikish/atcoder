S = input()

ans = 0
for i in range(len(S)):
    if S[i].isnumeric():
        ans = int(S[i:i + 2]) \
            if i < len(S) - 1 and S[i + 1].isnumeric() else int(S[i])
        break
print(ans)
