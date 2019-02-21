n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        if a[j] + a[i] > ans:
            ans = ans + 1
            break
print(ans)
