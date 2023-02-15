def solution(a, n):
	sum = 0
	if a[0] == "1":
		sum = 1
	signs = ""
	for i in range(1, n):
		if sum == 1 and a[i] == "1":
			signs += "-"
			sum = 0
		elif sum == 1 and a[i] == "0":
			signs += "+" 
			sum = 1
		elif sum == 0 and a[i] == "1":
			signs += "+"
			sum = 1  
		elif sum == 0 and a[i] == "0":
			signs += "+"
			sum = 0
	print(signs)

t = int(input())
for i in range(t):
	n = int(input())
	a = input()
	solution(a, n)