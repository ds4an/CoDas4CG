n = int(input())
a = list(map(int, input().split()))
for i in range(1, n + 1):
    for j in range(i + 1, -1, -1):
        if Jzzhu_STR_0_s[i] + a[i - 1] == 0:
            ans += 1
print(ans)
