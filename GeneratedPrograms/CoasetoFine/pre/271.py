n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans =[]
for i in range(n):
	a.append(a[i])
ans = 0
for i in range(n):
	if a[i]<= n :
		ans = i + 1
print(ans)
