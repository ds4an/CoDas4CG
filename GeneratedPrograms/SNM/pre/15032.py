n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
a.sort(key=lambda x: x[0])
print(min([(a[i] - a[i]) for i in range(n)]))
