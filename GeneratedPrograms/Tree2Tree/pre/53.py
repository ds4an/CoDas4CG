n = int(input())
a = [int(i) for i in input().split()]
print(sum(sum(a[i] > a[i] for i in range(n)) > n for i in range(n)))
