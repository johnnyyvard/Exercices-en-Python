#Rediger un programme python permettant de determiner si un nombre entier est pair ou non.
#Plus precisement, ecrivez une fonction "diviseurs" prenant en parametre
#le nombre entier "n"  et affichant le booleen vrai si "n" est pair, faux sinon.

def diviseurs(n):

	if n % 2 == 0: 
		print(True)
	else:
		print(False)

diviseurs(9)
diviseurs(10)

#Rediger un programme python permettant de determiner si un nombre entier est pair ou non.
#Plus precisement, ecrivez une procedure "diviseurs" prenant en parametre
#le nombre entier "n"  et affichant "le nombre" n " est pair" si c'est la cas,
#"le nombre " n " est impaire" sinon.

def diviseurs4(n):
	
	if n % 2 == 0:
		return "le nombre " + str(n) + " est pair"
	else:
		return "le nombre " + str(n) + " est impair"

print(diviseurs4(2))
print(diviseurs4(25))
 
