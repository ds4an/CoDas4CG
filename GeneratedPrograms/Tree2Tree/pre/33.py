n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(1, n + 1):
    ans += i * 2
print(ans)
