#...si l un est le double de l autre, ou si la variable booleenne 
#affiche prend la valeur vrai.

def afficheCond(a,b,affiche):

	if ((a==2*b)or(b==2*a)or affiche):
		return a+b
	else:
		return "rien"

print(afficheCond(2,3,True))
print(afficheCond(2,3,False))