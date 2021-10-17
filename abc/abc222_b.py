N, P = map(int, input().split())
a = list(map(int, input().split()))

print([ai < P for ai in a].count(True))
