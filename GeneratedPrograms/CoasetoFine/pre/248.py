n = int(input())
a = list(map(int, input().split()))
b =[]
ans = 0
ans = 0
for i in range(n):
	if a[i]!= i :
		ans += 1
		b.append(i)
ans = 0
for i in range(n):
	if a[i]> ans :
		ans = i + 1
if ans > 1 :
	print(ans)
else :
	print(ans)
