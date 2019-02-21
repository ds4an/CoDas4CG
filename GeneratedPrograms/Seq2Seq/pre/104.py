def main():
	n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b =[]
for i in range(n):
		a[i % 2]= a[i]% 2
b.append(a[i])
for i in range(n):
		if a[i]== 1 :
			a[i]= a[i]
else :
			a[i]= a[i]
if a[i]== 1 :
			a[i]= a[i]
b[i]= a[i]
if a[i]== 1 :
				a[i]= a[i]
b[i]= a[i]
else :
				a[i]= a[i]
if b[i]== 1 :
				a[i]= a[i]
b[i]= a[i]
print(max(a))
if __name__ == '__main__' :
	main()