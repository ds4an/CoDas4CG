n = int(input())
a = list(map(int, input().split()))
c = list(map(int, input().split()))
ans = 0
i = 0
for i in range(1, n + 1):
    if a[i] > a[i - 1]:
        c += 1
print(c)
