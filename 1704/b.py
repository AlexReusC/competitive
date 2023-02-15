

for _ in range(int(input())):
	n, x = list(map(int, input().split()))
	a = list(map(int, input().split()))

	changes = 0
	v = a[0]
	min_a = a[0]
	max_a = a[0]

	for i in range(1, n):
		min_a = min(min_a, a[i])
		max_a = max(max_a, a[i])
		v = min_a + ((max_a - min_a) // 2)
		# print(v)
		if(abs(v-min_a) > x or abs(v-max_a) > x):
			changes += 1
			min_a = a[i]
			max_a = a[i]

	print(changes)

		
