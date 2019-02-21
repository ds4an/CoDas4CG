n = int(input())
a = list(map(int, input().split()))
for i in range(1, n + 1):
    a[i] += a[i - 1]
m = int(input())
b = list(map(int, input().split()))
ans = 0
for i in range(n):
    ans += b[i] * b[i - 1]
print(ans)
