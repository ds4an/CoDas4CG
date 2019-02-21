I = lambda : map(int, input().split())
n, m = I()
a = list(I())
print(sum(a[i] + a[i - 1] for i in range(n)))
