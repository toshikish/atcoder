from collections import Counter

N = int(input())
a = list(map(int, input().split()))

C = Counter(a)
print(len(C.keys()))
