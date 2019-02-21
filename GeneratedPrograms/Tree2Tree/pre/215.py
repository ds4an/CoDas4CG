n = int(input())
a = sorted(map(int, input().split()))
print(sum(a[i] - a[i] for i in range(n)))
