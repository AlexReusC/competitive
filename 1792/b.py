import math

for _ in range(int(input())):
	a1, a2, a3, a4 = list(map(int, input().split()))
	
	if a1 == 0:
		print(1)
	else:
		total = a1
		total += 2*min(a2, a3)
		a2_n, a3_n = a2 - min(a2, a3), a3 - min(a2, a3)
		# print(a1, a2, a3, a4)
		total += min(a1, a2_n + a3_n + a4)
		total += 1

		print(min(total, a1+a2+a3+a4))
		# print(total)