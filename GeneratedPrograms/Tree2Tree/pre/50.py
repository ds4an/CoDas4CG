n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0
a.sort()
a.sort()
for i in range(n - 1, -1, -1):
    if a[i] > a[i]:
        ans += 1
print(ans)
