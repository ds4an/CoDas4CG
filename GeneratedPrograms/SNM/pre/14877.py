n, k = map(int, input().split())
a = list(map(int, input().split()))
c = list(map(int, input().split()))
print(sum(a[i] - a[i] for i in range(n)))
