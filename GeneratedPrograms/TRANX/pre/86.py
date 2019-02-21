n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
b = list(map(int, input().split()))
for i in range(n - 1, -1, -1):
    if a[i] < b[i]:
        print(a[i], end=' ')
        exit()
print(-1)