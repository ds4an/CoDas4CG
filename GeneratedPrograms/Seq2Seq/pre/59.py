n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans =[]
for i in range(n):
	if a <= b[i]:
		ans.append(a[i])
print(* ans)