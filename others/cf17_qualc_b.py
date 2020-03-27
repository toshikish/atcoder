N = int(input())
A = list(map(int, input().split()))

R = [Ai % 2 for Ai in A]
e = R.count(0)
print(3 ** N - 2 ** e)
