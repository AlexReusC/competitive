for _ in range(int(input())):
	n = int(input())

	digits_n = len(str(n))

	print((digits_n-1)*9 + (ord(str(n)[0])-ord('0')))
