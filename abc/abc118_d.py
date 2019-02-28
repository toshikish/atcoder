from operator import itemgetter
N, M = map(int, input().rstrip().split())
A = map(int, input().rstrip().split())
A.sort()
master = [2, 5, 5, 4, 5, 6, 3, 7, 6]
required = [master[a - 1] for a in A]
min_bars = 9
for i in range(len(A)):
    
