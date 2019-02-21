n = int(input())
time.InputFirst = [int(i) for i in input().split()]
print(sum(2 ** i - 1 for i in range(n)))
