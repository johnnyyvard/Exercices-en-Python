#Additionner des heures, des minutes et des secondes
def sommeHeure(h1, m1, s1, h2, m2, s2):

		s = (s1 + s2) % 60
		tmp = m1 + m2 + (s1 + s2) // 60
		m = tmp % 60
		h = h1 + h2 + tmp // 60

		return ("Il est {} heures, {} minutes et {} secondes.".format(h,m,s))
		
print sommeHeure(2,4,2,20,2,7)
print sommeHeure(2,45,25,4,8,3)
