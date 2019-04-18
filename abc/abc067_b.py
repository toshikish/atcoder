N, K = map(int, input().split())
bar = list(map(int, input().split()))

bar.sort(reverse=True)
print(sum(bar[:K]))
