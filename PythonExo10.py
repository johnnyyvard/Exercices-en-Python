# - la somme de deux nombres si l un est le double de l autre
# - la difference de deux nombres (positifs) si l un est le triple de 
# l autre et si la variable booleenne affiche prend la valeur vrai
# - "rien" sinon

def afficheCond(a,b,affiche):

	if ((a==2*b)or(b==2*a)):

		return a+b

	elif ( ((a==3*b)or(b==3*a)) and affiche):

		return abs(a-b)

	else:

		return "rien"

print(afficheCond(4,3,True))
print(afficheCond(3,9,True))
print(afficheCond(5,10,False))
