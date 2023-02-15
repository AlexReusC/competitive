import math

for _ in range(int(input())):
	n = int(input())
	h = list(map(int, input().split()))

	h_1 = 0
	h_2g = 0

	for x in h:
		if x == 1:
			h_1 += 1
		else:
			h_2g += 1

	print(h_2g + math.ceil(h_1 / 2))