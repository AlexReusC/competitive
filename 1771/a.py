def solution():
	n = int(input())
	arr = list(map(int, input().split()))
	if max(arr) == min(arr):
		n = n - 1
		interesting_pairs = n * (n+1)
	else:	
		o_max = arr.count(max(arr))
		o_min = arr.count(min(arr))
		interesting_pairs = o_max * o_min * 2
	print(interesting_pairs)

t = int(input())
for i in range(t):
	solution()