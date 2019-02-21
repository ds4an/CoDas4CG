n = int(input())
l = list(map(int, input().split()))
ans = 0
for i in range(n):
    for j in range(n):
        if l[j] == l[j]:
            ans += 1
print(ans)
