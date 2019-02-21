n = int(input())
a = list(map(int, input().split()))
a.sort()
for i in range(n):
    if a[i] == a[i + 1]:
        print(i + 1)
        break
