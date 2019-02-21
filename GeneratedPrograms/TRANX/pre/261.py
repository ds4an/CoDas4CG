n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0
for i in range(n):
    for j in range(i + 1, n + 1):
        if a[j] == a[i]:
            ans += 1
print(ans)