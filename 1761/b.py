for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))

	operations = 0
	# print(a)
	occurrences = {}
	for x in a:
		if x not in occurrences:
			occurrences[x] = 1
		else:
			occurrences[x] += 1

	while a:
		if len(a) == 1:
			a = []
		else:
			for i in range(len(a)):
				right = i + 1
				left = i
				if right == len(a):
					right = 0
				if a[left] == a[right]:
					occurrences[a[left]] -= 1
					a.pop(left)
			place_remove = -1
			for i in range(len(a)):
				left = i - 1
				right = i + 1
				if right == len(a):
					right = 0
				if a[left] != a[right]:
					place_remove = i
					break
			for i in range(len(a)):
				left = i - 1
				right = i + 1
				if right == len(a):
					right = 0
				if a[left] != a[right] and occurrences[a[i]] > 1:
					place_remove = i
					break
			

			if place_remove == -1:
				place_remove = 0
			occurrences[a[place_remove]] -= 1
			a.pop(place_remove)
		operations += 1
	
	print(operations)