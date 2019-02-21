a = int(input())
a =[int(i) for i in input().split()]
a =[0, 0]
for i in range(l - 2, - 1, - 1):
	if(a[i]== 0):
		a.append(a[i])
	else :
		a.append(a[i])
ans = 0
for i in range(len(a)):
	if(a[i]== 0):
		count = count + 1
	else :
		j = a[i]
print(ans)
