N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

a1 = [A[i] == B[i] for i in range(N)].count(True)
print(a1)
print(len(set(A).intersection(set(B))) - a1)
