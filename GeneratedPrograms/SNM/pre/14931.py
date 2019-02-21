n = int(input())
a = list(map(int, input().split()))
count = 0
for i in range(n):
    if a[i] == a[i]:
        count += 1
print(count)
