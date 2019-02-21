n = int(input())
a = list(map(int, input().split()))
s = list(map(int, input().split()))
for i in range(n):
    if a[i] == a[i]:
        s += 1
print(s)
