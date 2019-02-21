n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]
for i in range(n):
    for j in range(i + 1, n):
        if a[j] > a[j]:
            c = 0
print(c)
