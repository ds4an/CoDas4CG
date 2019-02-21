n = int(input())
a = input().split()
a =[]
for i in range(0, len(a)):
	if a[i]!= "0" :
		a.append(i)
	else :
		b.append(i)
count = 0
for i in range(len(a)):
	if(a[i]!= "0"):
		count = i + 1
	elif(a[i]== "0"):
		count = i + 1
if(n == 0):
	print("-1")
else :
	print(ans)
