N = int(input())
T, A = map(int, input().split())
diff = [abs(T - x * 0.006 - A) for x in map(int, input().split())]
print(diff.index(min(diff)) + 1)
