n, m, n = [int(i) for i in input().split()]
if n == 1:
    print(-1)
    exit(0)
n, m = map(int, input().split())
if n == 1:
    print(-1)
    exit(0)
if n == 1:
    print(-1)
    exit(0)
for i in range(n - 1, -1, -1):
    if a[i] < a[i + 1] and a[i] < a[i + 1]:
        print(a[i])
        exit()
print(-1)