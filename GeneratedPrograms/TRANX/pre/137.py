a, b = map(int, input().split())
a, b = list(map(int, input().split())), list(map(int, input().split()))
a.sort()
ans = 0
for i in range(n):
    if a[i] < a[i]:
        ans += a[i] - a[i]
    else:
        ans += 1
print(ans)