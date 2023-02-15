import math

for _ in range(int(input())):
	n = int(input())
	p = list(map(int, input().split()))

	m = math.ceil(n/2)

	m_it = -1
	for i in range(len(p)):
		if p[i] == m:
			m_it = i

	m_i = m + 1
	c_i = 0
	for i in range(m_it, len(p)):
		if p[i] == m_i:
			c_i += 1
			m_i += 1

	m_d = m - 1
	c_d = 0
	for i in range(m_it, -1, -1):
		if p[i] == m_d:
			c_d += 1
			m_d -= 1

	c_i = n - m - c_i
	c_d = m - 1 - c_d

	print(min(c_i, c_d) + abs(c_i - c_d))	