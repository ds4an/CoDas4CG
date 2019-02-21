n = int(input())
a = list(map(int, input().split()))
c = 0
c = 0
for i in range(n):
	if a[i]== - 1 :
		c += 1
	elif i - 1 >= 0 :
		c += 1
	else :
		c += 1
print(c)
