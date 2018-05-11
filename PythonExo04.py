#Si l'un est le double de l'autre.
#Sinon afficher "rien".

def afficheCond(a,b):
	
	if ((a==2*b)or(b==2*a)):
		return a+b
	else:
		return "rien"
	
print(afficheCond(6,3))
print(afficheCond(5,3))
