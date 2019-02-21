n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split('')]
print(sum((2 * a[i] - a[i - 2]) * 2 ** i - 2 for i in range(n)))
