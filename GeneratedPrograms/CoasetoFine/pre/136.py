n, b = map(int, input().split())
a = list(map(int, input().split()))
d =[0]* n
d =[0]* n
d =[0]* n
d =[0]* n
d =[0]* n
d =[0]* n
ans =[0]* n
s = 0
for i in range(n):
	if a[i]:
		count = i - 1
		j = 1
		while j < n :
			if arr[j]:
				count += 1
				ans.append(j)
				j += 1
			else :
				a[j]= 0
				ans += 1
ans = 0
for i in arr :
	ans += i
print(ans)
