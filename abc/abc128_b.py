N = int(input())
r = {}
for i in range(N):
    Si, Pi = input().split()
    Pi = int(Pi)
    r[(Si, -Pi)] = i + 1

for t in sorted(r.keys()):
    print(r[t])
