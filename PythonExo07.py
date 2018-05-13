#...pairs d'un chiffre.

import math

def divise(n,p):
#n divise p

	if abs (n) > abs (p) :
		n , p = p , n
	return (p%n ==0)

def afficheDiviseursListePairs(n):

	ListeDiv = []
	max = int(math.sqrt(n))

	for i in range(1,max+1):

		if divise(i,n) :

			if i%2==0:

				ListeDiv.append(i)
				ListeDiv.append(-i)
			
			if (n//i)%2==0:
			
				ListeDiv.append(n//i)
			
				ListeDiv.append(-(n//i))
		
		ListeDiv.sort()
	
	print(ListeDiv)

afficheDiviseursListePairs(10)
afficheDiviseursListePairs(50)