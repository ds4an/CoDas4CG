n = int(input())
a =[int(i)for i in input().split()]
a =[]
for i in range(7):
	a.append(sum(a[i : i + 7]))
for i in range(7):
	a[i]= a[i]+ a[i]
print(sum(a))