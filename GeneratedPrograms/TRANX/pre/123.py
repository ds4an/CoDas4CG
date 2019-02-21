n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
b = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0
for i in range(1, len(a)):
    ans += abs(a[i] - a[i - 1])
    a[i - 1] -= 1
    ans += 1
print(ans)