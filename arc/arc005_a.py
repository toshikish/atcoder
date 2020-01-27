N = int(input())
w = list(input().rstrip('.').split())

d = ['TAKAHASHIKUN', 'Takahashikun', 'takahashikun']
print(sum(w.count(di) for di in d))
