def afficheCond(a,b):

	if ((a==2*b)or(b==2*a)):
		return a+b
	else:
		return "rien"

print(afficheCond(6,3))
print(afficheCond(6,2))
print(afficheCond(10,5))