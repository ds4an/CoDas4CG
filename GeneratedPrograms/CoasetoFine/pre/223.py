n, k = map(int, input().split())
a = list(map(int, input().split()))
s = list(map(int, input().split()))
ans = 0
ans = 0
ans = 0
for i in range(2 * n):
	if(a[i]* a[i])% k != 0 :
		f = True
		break
if f :
	print("-1")
else :
	for i in range(n):
		if a[i]!= a[i]:
			f = 1
			break
	if f == 1 :
		print("-1")
		exit()
print("-1")
