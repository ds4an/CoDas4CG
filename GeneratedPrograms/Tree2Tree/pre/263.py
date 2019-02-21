n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    a[i] = int(a[i])
n -= 1
print(sum(a))
