#est le double d'un autre

import math

def divise(n,p):
#n divise p

	if abs (n) > abs (p) :
		n , p = p , n
	return (p%n ==0)

print divise(5,10)
print divise(9,2)
