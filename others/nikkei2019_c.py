N = int(input())
D = [tuple(map(int, input().split())) for i in range(N)]

print(sum(sorted([d[0] + d[1] for d in D], reverse=True)[::2])
      - sum([d[1] for d in D]))
