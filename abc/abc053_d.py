N = int(input())
A = list(map(int, input().split()))

k = len(set(A))
print(k - (k + 1) % 2)
