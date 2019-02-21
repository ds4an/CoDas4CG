from = int(input())
a = input().split()
b =[int(x) for x in a]
ans = 0
for i in range(len(a)- 1):
	c = i + 1
	while a[j]== a[j + 1]:
		j += 1
	if c == n :
		print(i + 1)
		exit()
print("-1")
