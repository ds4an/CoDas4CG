n = int(input())
t =[]
for i in range(n):
	t.append(list(map(int, input().split())))
ans = 0
ans = 0
for i in range(n):
	if a[i]== a[i]:
		k = 1
		break
if ans == 1 :
	print(ans)
else :
	ans = 0
	ans = 0
	for i in range(n):
		if a[i]% d != 0 :
			ans = i
			break
	if ans == 1 :
		print(ans)
	else :
		print(pow(2, n - d))
