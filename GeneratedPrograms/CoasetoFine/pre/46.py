n = input().split()
n = int(n[0])
m = int(n[1])
a =[]
for i in range(n):
	a.append(input().split())
a = a.split()
ans = 0
for i in range(len(a)):
	if(a[i]== a[- 1]):
		ans = ans + a[- 1]
	else :
		ans = i + 1
print(ans)
