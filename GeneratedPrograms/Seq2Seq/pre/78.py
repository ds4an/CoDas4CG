n = int(input())
p =[0]* 4
for i in range(1, n):
	p[i]= p[i % 3]% 3
p[i]= p[i - 1]% 3
p =[0]* 4
for i in range(1, n):
	p[i]= p[i - 1]% 3
p[i]= p[i]% 3
p =[0]* 4
for i in range(1, n):
	p[i]= p[i - 1]% 3
p[i]= p[i]% 3
print(* p)