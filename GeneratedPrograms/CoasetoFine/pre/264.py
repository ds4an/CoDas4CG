n = int(input())
a = list(map(int, input().split()))
r =[]
for i in range(n - k + 1):
	x = a.index(a[i])
	if(i - a[i - 1])<= 1 :
		r.append(i)
print(len(r))
print(" ".join(t))
