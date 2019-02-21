m, m, a, b = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
b = list(map(int, input().split()))
for i in range(len(a) - 1, -1, -1):
    if a[i] < a[i + 1]:
        a[i] = a[i + 1] - a[i]
    elif a[i] < a[i + 1]:
        a[i + 1] = a[i + 1] - a[i]
    elif a[i] < a[i + 1]:
        a[i + 1] = a[i + 1] - a[i]
print(min(a))