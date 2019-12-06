N = int(input())
S = [list(map(int, input().split())) for i in range(N)]
print(max([sum(s[0:4]) + s[4] * 110 / 900 for s in S]))
