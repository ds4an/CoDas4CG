t = int(input())
arr = list(map(int, input().split()))
ans =[]
for i in range(n):
	arr.append(a[i])
ans = 0
for i in range(n):
	s = arr[i]
	if(s > ans):
		ans = s
		ans = i
print(count)
