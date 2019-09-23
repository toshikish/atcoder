N = int(input())
A = map(int, input().split())

B = [ai for ai in A if ai > 0]
l = len(B)
print((sum(B) + l - 1) // l)
