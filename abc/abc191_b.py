N, X = map(int, input().split())
A = list(map(int, input().split()))
print(' '.join([str(Ai) for Ai in A if Ai != X]))
