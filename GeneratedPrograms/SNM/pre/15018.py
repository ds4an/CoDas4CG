n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for i in range(n):
    a[i] = max(a[i], a[i])
print(max(a))
