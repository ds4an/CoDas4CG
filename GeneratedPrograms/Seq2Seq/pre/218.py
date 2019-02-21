n = int(input())
a =[input()for i in range(n)]
for i in range(n - 1):
	if a[i][0]== a[i + 1][0]:
		print(i + 1)
exit()
print(- 1)