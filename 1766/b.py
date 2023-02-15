def solution():
	n = int(input())
	s = input()
	if n <= 3:
		print("NO")
		return

	mySet = {s[0:1]}

	for i in range(3, n+1):
		if s[i-2:i] in mySet:
			print("YES")
			return
		mySet.add(s[i-3:i-1])
	print("NO")

t = int(input())
for i in range(t):
	solution()