n = int(input())
a = list(map(int, input().split()))
s = sum(a[i] + a[i + 1] for i in range(n))
s = sum(a[i] + a[i + 1] for i in range(n - 1))
if n % 2 == 0:
    s += 1
print(s)
