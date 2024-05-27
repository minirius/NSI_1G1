def plus_grand_v1(a, b, c):
	if a < b:
		if a > c:
			return a
		else:
			return c
	else:
		if b > c:
			return b
		else:
			return c

def plus_grand_v2(a, b, c):
	if a > b and a > c:
		return a
	elif b > a and b > c:
			return b
	else:
			return c