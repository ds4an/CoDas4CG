n = int(input())
a = [int(x) for x in input().split()]
c = 0
for i in range(n):
    for j in range(i + 1, -1, -1):
        if for[i] > a[j]:
            c += 1
print(c)
