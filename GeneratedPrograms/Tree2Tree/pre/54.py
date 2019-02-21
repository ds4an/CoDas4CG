n = int(input())
a = [int(i) for i in input().split()]
print(sum(a[i] - a[i - 1] for i in range(n)))
