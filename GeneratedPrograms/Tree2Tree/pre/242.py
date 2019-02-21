n = int(input())
a = [int(x) for x in input().split()]
print(sum(a[i] > a[i] for i in range(n)))
