n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for i in range(n):
	for j in range(i):
		if a[i]== a[j]:
			b[j]= a[j]
b[j]= a[j]
print(* a)