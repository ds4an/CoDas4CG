n, a, b = map(int, input().split())
a = list(map(int, input().split()))
b =[]
for i in range(n):
	a.append(int(input()))
a.sort()
b.sort()
a.sort()
b =[]
for i in range(n):
	a.append(a[i]// 2)
a.sort()
b.sort()
if(a[- 1]== 2):
	print(- 1)
else :
	print(a[- 1])