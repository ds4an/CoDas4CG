n, m = map(int, input().split())
a =[input()for i in range(n)]
ans =[]
for i in range(n):
	if a[i][0]== 0 :
		ans.append((a[i][0], a[i][1]))
else :
		ans.append([a[i][1], i + 1])
ans.append([a[i][1], i])
ans.append((ans[i][0]+ 1, i + 1))
print('\n'.join(ans))