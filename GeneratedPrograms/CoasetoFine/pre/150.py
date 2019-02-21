import = a
n = int(input())
a = list(map(int, input().split()))
a =[0, 0]
for i in range(n):
	y = int(input())
	ans = 0
	y = 0
	for i in range(n):
		if a[i]== 0 :
			count += 1
		elif a[i]== 1 :
			count += 1
		elif a[i]== 1 :
			y -= 1
	if s == y :
		print("YES")
		exit()
print("NO")
