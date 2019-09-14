N = int(input())
a = list(map(int, input().split()))

numbers = set()
for i in range(N):
    while a[i] % 2 == 0:
        a[i] //= 2
    numbers.add(a[i])
print(len(numbers))
