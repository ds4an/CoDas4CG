n = int(input())
a = list(map(int, input().split()))
b =[0]*(n + 1)
for i in range(n):
	if a[i]== a[i - 1]:
		a[i]= a[i - 1]+ 1
else :
		a[i]= a[i - 1]+ 1
a[i]= a[i - 1]+ 1
a[i]= a[i - 1]+ 1
print(max(a))