n = int(input())
a = [int(x) for x in input().split()]
print(sum(sum(a[i] > a[i + 1] for i in range(n)) > n for i in range(n)))
