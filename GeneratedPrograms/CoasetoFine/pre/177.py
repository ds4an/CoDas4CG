def main():
	n, m = map(int, input().split())
	a = list(map(int, input().split()))
	a =[]
	for _ in range(n):
		s = input()
		a.append(s)
	a =[]
	count = 0
	ans = 0
	for i in range(n):
		if a[i]== a[i]:
			count += 1
		if a[i]== i :
			count += 1
		if a[i]== i :
			ans.append(a[i])
	if len(ans)== 0 :
		print(d)
	else :
		print(d)
