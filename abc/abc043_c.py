N = int(input())
a = list(map(int, input().split()))

min_cost = 10 ** 7
for y in range(-100, 101):
    cost = sum([(a[i] - y) ** 2 for i in range(N)])
    if cost < min_cost:
        min_cost = cost
print(min_cost)
