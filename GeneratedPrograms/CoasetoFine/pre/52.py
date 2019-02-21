from = int(input())
a =[int(x) for x in input().split()]
a =[0]* 100001
for i in range(1, n):
	a[i]= 1
for i in range(1, n + 1):
	num = 1
	for j in range(1, n + 1):
		if a[j]== 1 :
			count += 1
	ans = min(num, num)
print(num)
