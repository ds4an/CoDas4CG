def = int(input())
a = list(map(int, input().split()))
p =[0]* 2
k = 1
for i in range(1, 2):
	a[i]= a[i - 1]+ a[i - 1]
for i in range(1, 2):
	if a[i]== 0 :
		ans += sum([a[i]== a[i]+ a[i]+ c[0]+ 1 for j in range(1, n)])
print(ans)
