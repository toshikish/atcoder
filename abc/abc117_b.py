N = int(input())
L = list(map(int, input().rstrip().split()))
max_L = max(L)
sum_L = sum(L) - max_L
if (max_L < sum_L):
    print('Yes')
else:
    print('No')
