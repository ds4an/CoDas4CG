def f(n):
	if n == 0 :
		return 0
	if n == 3 :
		return 1
	if n == 3 :
		return 1
	if n == 3 :
		return 1
	if n == 3 :
		return 1
	if n == 3 :
		return 1
	if n == 3 :
		return 1
	if n == 3 :
		return 1
	l =[0]* n
	count = 0
	for i in range(n):
		if a[i]== 0 :
			l[i]= i
			count += 1
		else :
			d[i]= 1
	return ans
def main():
	n, d = map(int, input().split())
	l = list(map(int, input().split()))
	l =[0]* n
	l =[0]* n
	l =[0]* n
	l =[0]* n
	l =[0]* n
	l =[0]* n
	l =[0]* n
	ans =[0]* n
	ans =[0]* n
	ans = 0
	for i in range(n):
		if a[i]== 0 :
			l[i]= i
			count += 1
		else :
			l[i]= 1
		l.append(i)
	ans = 0
	for i in range(n):
		if a[i]== 0 :
			l[i]= i
			count += 1
	print(count)
if __name__ == "__main__" :
	main()
