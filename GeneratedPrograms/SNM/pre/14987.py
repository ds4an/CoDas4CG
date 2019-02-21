n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
b = list(map(int, input().split()))
for i in range(n):
    b[i] = int(b[i])
print(sum(a[i] - b[i] for i in range(n)))
