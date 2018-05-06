#Ecrire un programme qui affiche la somme de deux nombres si l un est le double de
#l autre, "rien" sinon.

def afficheCond(a,b):
	if ((a==2*b)or(b==2*a)):
		return a+b
	else:
		return "rien"
print(afficheCond(6,3))
