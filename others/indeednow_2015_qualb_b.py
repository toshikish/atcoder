s = input()
t = input()

N = len(s)
for i in range(N):
    if s[N - i:] + s[:N - i] == t:
        ans = i
        break
else:
    ans = -1
print(ans)
