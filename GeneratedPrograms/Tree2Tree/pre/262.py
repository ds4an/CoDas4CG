n = int(input())
a = [int(x) for x in input().split()]
a.sort()
print(sum(a[i] - a[i - 1] for i in range(n)))
