n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans =[]
s = 0
for i in range(n):
	if a[i]> s :
		ans.append(i)
if len(s)< n :
	print(s.count(a[i]))
else :
	print(- 1)
