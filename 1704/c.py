for _ in range(int(input())):
	n, m = list(map(int, input().split()))
	a = list(map(int, input().split()))

	a.sort()
	distances = []
	for i in range(1, m):
		distances.append(a[i]-a[i-1]-1)
	distances.append((n-a[-1])+(a[0]-1))

	distances.sort(reverse=True)
	non_infected_houses = 0
	for i in range(0, len(distances)):
		if distances[i] - 4*i - 1 < 0:
			break
		elif distances[i] - 4*i - 1 == 0:
			non_infected_houses += 1
		non_infected_houses += distances[i] - 4*i - 1 

	print(n - non_infected_houses)