n = int(input())
a =[int(i)for i in input().split()]
b =[int(i)for i in input().split()]
b =[int(i)for i in input().split()]
if n == 1 :
	print(- 1)
exit(0)
for i in range(n):
	if a[i]== b[i]:
		print(i + 1)
break
else :
	print(- 1)