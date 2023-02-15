import math

for _ in range(int(input())):
	n = int(input())
	number = int(input())
	number_str = str(number)
	first_digit = number_str[0]
	# print(first_digit)

	if first_digit != "9":
		print(int('9' * n) - number)
	else:
		print(int('1' * (n+1)) - number)
