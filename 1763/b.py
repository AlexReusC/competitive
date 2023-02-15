def solution():
	n, k = list(map(int, input().split()))
	h = list(map(int, input().split()))
	p = list(map(int, input().split()))

	occurrences = {}
	p_unique = []
	for x in p:
		if x in occurrences:
			occurrences[x] += 1
		else:
			occurrences[x] = 1
			p_unique.append(x)

	p_unique.sort()
	tuples_sorted = sorted(zip(h, p))
	tuples_sorted = zip(*tuples_sorted)
	h, p = [list(tuple) for tuple in tuples_sorted]

	# print(h, p)

	ptr = 0
	ptr_unique = 0
	total_k = k	
	minimun_power = p_unique[ptr_unique]
	while ptr < n:
		# print(ptr, k, total_k, minimun_power)
		if k <= 0:
			print("NO")
			return
		if h[ptr] > total_k:
			k -= minimun_power
			total_k += k
		else:
			occurrences[p[ptr]] -= 1
			while occurrences[p_unique[ptr_unique]] == 0:
				ptr_unique += 1
				if ptr_unique == len(p_unique):
					break
			if ptr_unique != len(p_unique):
				minimun_power = p_unique[ptr_unique]
			ptr += 1

	print("YES")


for _ in range(int(input())):
	solution()
