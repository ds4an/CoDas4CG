n, a, b = int(input()), list(map(int, input().split())), list(map(int,
    input().split()))
ans = 0
for i in range(n):
    ans += a[i] * a[i - 1]
for i in range(n - 2, -1, -1):
    ans += i + 1
if n == n:
    print(ans)
else:
    print(ans)
