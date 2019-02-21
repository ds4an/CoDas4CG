n = input()
n = len(a)
a =[int(x) for x in input().split()]
ans = 0
ans = 0
ans =[]
for i in range(0, n):
	if a[i]!= a[i - 1]: s.append(i)
ans = 0
for i in range(0, n):
	if a[i]% 10 == 0 : ans = a[i]
	elif a[i]!= i : ans = i
if cnt == 0 : print(ans)
else :
	ans = 0
	for i in range(n):
		if a[i]!= 0 : ans = a[i]
		ans = i + 1
	if c == 0 :
		print(ans)
	else :
		print(ans)
