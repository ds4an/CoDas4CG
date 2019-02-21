n = int(input())
a = list(map(int, input().split()))
n = int(input())
n -= 1
print(sum(a[i] * a[i] for i in range(n)))
