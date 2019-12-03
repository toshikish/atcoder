N = int(input())
m = list(map(int, input().split()))
print(sum([max(80 - mi, 0) for mi in m]))
