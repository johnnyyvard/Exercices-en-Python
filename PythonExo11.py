# ... type integer et qui affiche:
# - le nombre nb si nb est impair
# - le nombre nb/2 si nb est pair
# - le message "attention" si le nombre nb est negatif

def afficheCond(a):

	resultat = ""
	
	if a<0:
	

		resultat = "attention ! "

	if (a%2)==0:
	
		resultat += str(a/2)
	
	else:
	
		resultat += str(a)
	
	return(resultat)	

print(afficheCond(-5))
print(afficheCond(10))