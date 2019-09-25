N = int(input())
s = input()
t = input()

l = 0
for n in range(N, 0, -1):
    if s[N - n:] == t[:n]:
        l = n
        break
print(2 * N - l)
