N = int(input())
S = [sum(list(map(int, input().split()))) for i in range(N)]

print(len(list(filter(lambda s: s < 20, S))))
