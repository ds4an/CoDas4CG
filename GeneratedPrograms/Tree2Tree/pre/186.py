n = int(input())
a = list(map(int, input().split()))
s = sum(a[i] + a[i + 1] for i in range(1, n + 1))
if s > s:
    s = s
print(s)
