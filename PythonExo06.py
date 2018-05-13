#...des diviseurs positifs d'un chiffre.

import math

def divise(n,p):
#n divise p

	if abs (n) > abs (p) :
		n , p = p , n
	return (p%n ==0)

def afficheDiviseursListe(n):

	ListeDiv = [1,n]
	max = int(math.sqrt(n))

	for i in range(2,max+1):

		if divise(i,n) :

			ListeDiv.append(i)
			ListeDiv.append(n//i)

		ListeDiv.sort()

	print(ListeDiv)

afficheDiviseursListe(5)
afficheDiviseursListe(100)