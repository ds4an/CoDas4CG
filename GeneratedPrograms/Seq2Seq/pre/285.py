n = int(input())
a =[0]*(sum(a))
b =[0]*(sum(a))
for i in range(n):
	c[a[i]]= c[i - 1]
for i in range(n):
	c[i]= c[i]- c[i]
print(sum(c))