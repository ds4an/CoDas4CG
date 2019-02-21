n, k = 0, 0
n = int(input())
t =[int(x) for x in input().split()]
x =[int(x) for x in input().split()]
l.sort()
for i in range(1, n):
	if(t[i]>= k):
		ans += 1
		k += 1
	if(t[i]== k):
		count += 1
if(k == 2):
	print(ans)
else :
	print(0)
