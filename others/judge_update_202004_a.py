S, L, R = map(int, input().split())
print(S if L <= S <= R else L if S < L else R)
