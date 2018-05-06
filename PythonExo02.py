#Ecrire un algorithme permettant de calculer le enieme terme de la suite de Fibonacci.

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

#Ecrire un algorithme permettant de determiner si un nombre entier positif est un multiple
#d'un autre nombre.

import math

def divise(n,p):
#n divise p

	if abs (n) > abs (p) :
		n , p = p , n
	return (p%n ==0)

print divise(5,10)
print divise(9,2)

#Ecrire un algorihtme permettant d'afficher la liste des diviseurs positifs d'un chiffre.
#Entree: un nombre entier positif.
#Sortie: une chaine de caracteres.
#Sous forme de liste.

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

#Ecrire un algorihtme permettant d'afficher la liste des diviseurs pairs d'un chiffre.

def afficheDiviseursListePairs(n):
	ListeDiv = []
	max = int(math.sqrt(n) )
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