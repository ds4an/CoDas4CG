n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
d = { }
for i in range(n):
	d[a[i]]= i
for i in range(n):
	d[i]= max(d[i], d[i])
print(max(d.values()))