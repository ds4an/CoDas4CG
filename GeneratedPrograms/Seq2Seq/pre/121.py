n = int(input())
a = list(map(int, input().split()))
for i in range(n):
	if a[i]== 0 :
		print(i + 1)
break
else :
	print(0)