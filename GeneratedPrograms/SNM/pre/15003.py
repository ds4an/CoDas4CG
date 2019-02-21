n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    a[i] = max(a[i], a[i - 1])
ans = 0
print(ans)
for i in range(n):
    print(a[i], end='')
