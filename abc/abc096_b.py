L = list(map(int, input().split()))
K = int(input())

maximum = max(L)
print(sum(L) - maximum + maximum * 2 ** K)
