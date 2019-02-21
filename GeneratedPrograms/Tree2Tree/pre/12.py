n = int(input())
a = list(map(int, input().split()))
c = list(map(int, input().split()))
n -= 1
print(sum(a[i] - a[i - 1] for i in range(n)))
