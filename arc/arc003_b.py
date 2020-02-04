N = int(input())
s = []
for i in range(N):
    si = input()
    s.append((si[::-1], si))

s.sort()
for i in range(N):
    print(s[i][1])
