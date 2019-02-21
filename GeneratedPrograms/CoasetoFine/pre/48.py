n, m = map(int, input().split())
s = list(map(int, input().split()))
s =[x for i in range(n)if s[i]!= t[i]]
ans =[i for i in range(n)if s[i]!= t[i]]
ans =[i for i in range(n)if s[i]!= s[i]]
ans =[i for i in range(n)if s[i]!= s[i]]
for i in range(n):
	if s[i]!= s[i]:
		s[i]= i + 1
print(ans)
