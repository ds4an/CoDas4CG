n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    a[i] += 1
for i in range(n - 2, -1, -1):
    print(a[i], end='')
if i % 2 == 0:
    print(-1)
