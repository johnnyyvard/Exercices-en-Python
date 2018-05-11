def fibbo(n):

	val1 = 1
	val2 = 1

	if n < 2:
		result = 1
	else:
		for i in range(1,n):
			result = val1 + val2
			val1 = val2
			val2 = result
	return(result)

print fibbo(7)
print fibbo(5)
print fibbo(3)