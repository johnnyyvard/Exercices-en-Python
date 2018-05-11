#Plus precisement, ecrivez une fonction "diviseurs" prenant en parametre
#le nombre entier "n" et affichant le booleen vrai si "n" est pair, faux sinon.

def diviseurs(n):

	if n % 2 == 0: 
		print(True)
	else:
		print(False)

diviseurs(9)
diviseurs(10)