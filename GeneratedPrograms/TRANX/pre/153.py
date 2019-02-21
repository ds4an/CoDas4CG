n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
b = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0
for i in range(n - 1, -1, -1):
    ans += abs(a[i] - a[i - 1])
print(ans)