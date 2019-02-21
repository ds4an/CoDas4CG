n = int(input())
used = [int(i) for i in input().split()]
print(sum(2 ** i - 2 ** i - 1 for i in range(n)))
