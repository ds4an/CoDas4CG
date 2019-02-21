n, m, l, r = map(int, input().split())
if n != 1 :
	print('NO')
else :
	for i in range(n):
		ans =[]
for j in range(n):
			if l[j]== l[i]:
				ans.append(l[j])
if l[i]== l[j]:
				ans.append(l[i])
if len(ans)== 0 :
	print('NO')
else :
	print('YES')
print(* ans)