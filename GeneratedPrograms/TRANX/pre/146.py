a = list(map(int, input().split()))
b = list(map(int, input().split()))
b = list(map(int, input().split()))
b = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0
for i in range(len(s) - 1, -1, -1):
    if s[i] == s[i + 1]:
        ans += 1
print(ans)