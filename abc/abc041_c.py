N = int(input())
a = list(map(int, input().split()))

b = [(a[i], i + 1) for i in range(N)]
b.sort(reverse=True)
for bi in b:
    print(bi[1])
