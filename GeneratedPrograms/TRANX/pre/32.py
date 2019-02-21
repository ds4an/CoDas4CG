I = lambda : list(map(int, input().split()))
n = int(input())
a = list(map(int, input().split()))
c = [0] * (n + 1)
for i in range(n):
    for j in range(n):
        if a[i] == a[i] and a[i] == a[i + 1]:
            print(a[i], end=' ')
    print()