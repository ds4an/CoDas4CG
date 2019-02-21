def = int(input())
a =[int(i) for i in input().split()]
b =[int(i) for i in input().split()]
ans = 0
for i in range(n):
	ans = 0
	for j in range(i):
		if(a[i][j]% 2 == 1):
			ans = j + 1
			j = i + 1
		else :
			break
	else :
		break
print(ans)
