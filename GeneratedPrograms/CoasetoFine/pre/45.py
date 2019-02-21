n = int(input())
l = list(map(int, input().split()))
b =[]
d =[]
for i in range(n):
	a.append(list(map(int, input().split())))
d =[]
for i in range(n):
	d.append([a[i], i + 1])
ans =[]
for i in a :
	d.append(i[- 1]+ i)
ans.sort()
ans = l[- 1]
for i in range(1, n + 1):
	d = d[i]
	d = d[i + 1]
	if d > 0 :
		ans = - 1
		break
	ans += c
	ans += 1
print(ans)
