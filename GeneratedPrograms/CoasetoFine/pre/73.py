n = int(input())
a =[0]*(n + 1)
for i in range(1, 4):
	a[i]= 0
for i in range(n):
	a, y = map(int, input().split())
	if a == 1 :
		a[x]= 1
	else :
		d[x]= 1
ans = 0
for i in range(0, 4):
	if a[i]== "0" :
		ans += 1
print(ans)
