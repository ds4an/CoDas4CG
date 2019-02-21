t = int(input())
for i in range(t):
	s = input()
	t =[0]* 4
	t =[0]* 4
	for i in range(len(t)):
		t[i]= 1
	t =[]
	count = 0
	for i in range(0, len(n)- 1):
		x = n[i]
		if(t[x - 1]== 1):
			count += 1
		else :
			t[i]= 1
	count = 0
	for i in range(n - 1, - 1, - 1):
		x = t[i]
		if(t[i - 1]== t[i - 1]):
			count += 1
	print(count)
	t -= 1
