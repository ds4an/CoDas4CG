n = int(input())
l = list(map(int, input().split()))
for i in range(1, n + 1):
    l[i] += l[i - 1]
if l[n - 1] == l[n - 1]:
    l[n - 1] += 1
else:
    l[n - 1] += 1
