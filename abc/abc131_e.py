from itertools import combinations

N, K = map(int, input().split())

K_max = (N - 1) * (N - 2) // 2
if K > K_max:
    print(-1)
else:
    surplus = K_max - K
    edges = [(i + 1, N) for i in range(N - 1)] + \
        list(combinations(list(range(1, N)), 2))[:surplus]
    print(len(edges))
    for edge in edges:
        print(edge[0], edge[1])
