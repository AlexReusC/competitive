for _ in range(int(input())):
	n, a, b =  list(map(int, input().split()))

	if b < a:
		print(1)
	else:
		if n % a == 0:
			print(n//a)
		else:
			print(n//a+1)