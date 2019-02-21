n, k = map(int, input().split())
a = list(map(int, input().split()))
for i in range(n):
    if a[i] == a[i]:
        print(a[i])
        exit()
print(-1)