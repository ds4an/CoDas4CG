n = int(input())
color = [int(i) for i in input().split()]
print(sum((n - i - 1) // i for i in range(n)))
