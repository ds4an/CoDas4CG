n, m = map(int, input().split())
a = list(map(int, input().split()))
print(min(a[i] - a[i] for i in range(n)))