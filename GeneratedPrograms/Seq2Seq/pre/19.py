n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
b =[]
for i in range(n):
	b.append([])
for j in range(i + 1, n):
		if a[j]== b[i]:
			b.append(a[j])
else :
			b.append(a[j])
print(* a)