n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
b = max(a)
print(max(a[i] - a[i] for i in range(n)))
