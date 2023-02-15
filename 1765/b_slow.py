for _ in range(int(input())):
	n = int(input())
	a = 1
	b = n - 1
	lcm = b
	for i in range(n):
		tmp_lcm = float("inf")
		if a == b:
			tmp_lcm = a
		elif a > b and b % a == 0:
			tmp_lcm = a
		elif b > a and a % b == 0:
			tmp_lcm = b
		else:
			tmp_lcm = a * b
		lcm = min(lcm, tmp_lcm)

	print(lcm)