a = int(input())
b = list(map(int, input().split()))
print(sum(a[i] - a[i - 1] for i in range(n - 1)))
