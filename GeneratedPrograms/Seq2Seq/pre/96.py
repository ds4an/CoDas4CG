n = int(input())
a =[int(x)for x in input().split()]
a =[]
for i in range(n):
	a.append([])
for i in range(n):
	a[i]=[0]*(n - 1)
for i in range(n):
	if a[i][0]== a[i][1]:
		print("YES")
exit()
print("NO")