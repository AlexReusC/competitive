for _ in range(int(input())):
	n = int(input())

	a = 1
	lcm = float("inf")
	for i in range(2, int(n ** 0.5)):
		print(n, i)
		if a  < lcm:
			lcm = 
			a = i
	
	print(a, n-a)