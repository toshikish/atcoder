N = int(input())
a = list(map(int, input().split()))

print(sum(i % 2 == 0 and a[i] % 2 == 1 for i in range(N)))
