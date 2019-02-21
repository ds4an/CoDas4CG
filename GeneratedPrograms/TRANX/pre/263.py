n = int(input())
a = []
for i in range(n):
    a.append(input())
ans = 0
for i in range(1, len(a) + 1):
    if a[i] == a[i]:
        ans += 1
print(ans)