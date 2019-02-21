n = int(input())
l = list(map(int, input().split()))
for i in range(1, n + 1):
    l[i] = min(l[i - 1], l[i - 1])
l[n - 1] = min(l[i - 1], l[i - 1])
l[n - 1] = min(l[n - 1], l[n - 1])
l[n - 1] = l[n - 1] + l[n - 1]
n = int(input())
for i in range(1, n + 1):
    l[i] += l[i - 1]
print(''.join(map(str, l)))
