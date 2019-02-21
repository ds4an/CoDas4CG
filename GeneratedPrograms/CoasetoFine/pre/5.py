n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
p =[0]*(n + 1)
p =[0]*(n + 1)
for i in range(n):
	if a[i]== 1 :
		a[i]= a[i - 1]+ 1
		a[i]= 1
	else :
		a[i]= 1
count = 0
for i in range(n):
	if a[i]== 1 :
		count += 1
		a[i]= a[i]
	else :
		p[i]= a[i]+ 1
count = 0
for i in range(n):
	if a[i]== 1 :
		count += 1
		j = a[i]
print(ans)
