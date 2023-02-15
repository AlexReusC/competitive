def solution():
	result = []
	n, k = list(map(int, input().split()))
	increase = 1
	k_i = 1
	for i in range(n):
		result.append(k_i)
		k_i += increase
		increase += 1
	
	ptr_end = n - 1
	
	while True:
		if result[n-1] <= k:
			break
		for i in range(ptr_end, n):
			result[i] = result[i-1] + 1
		ptr_end -= 1

	print(*result)

t = int(input())
for i in range(t):
	solution()