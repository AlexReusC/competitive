#create dictionary
#start in lowest, create sets, start lowering appearences

for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))

	occurrences_a = dict()
	for x in a:
		if x in occurrences_a:
			occurrences_a[x] += 1
		else:
			occurrences_a[x] = 1
	
	elems = list(occurrences_a.keys())
	elems.sort()
	# print(elems)
	
	sets = 0
	for x in elems:
		while occurrences_a[x] > 0:
			sets += 1
			occurrences_a[x] -= 1
			increment = 1
			while x+increment in occurrences_a and occurrences_a[x+increment] != 0:
				occurrences_a[x+increment] -= 1
				increment += 1

	print(sets)