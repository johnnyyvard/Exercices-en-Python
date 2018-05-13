#...est pair ou non.
#Plus precisement, ecrivez une procedure "diviseurs" prenant en parametre
#le nombre entier "n" et affichant "le nombre" n " est pair" 
#si c'est la cas, "le nombre " n " est impaire" sinon.

def diviseurs4(n):
	
	if n % 2 == 0:
		return "le nombre " + str(n) + " est pair"
	else:
		return "le nombre " + str(n) + " est impair"

print(diviseurs4(2))
print(diviseurs4(25))