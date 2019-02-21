n = int(input())
a = [int(i) for i in input().split()]
print(sum(2 ** i - 2 ** i for i in range(n)))
