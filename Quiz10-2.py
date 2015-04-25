def mul():
	x1=[]
	x2=[]
	t=0
	for i in range(0,5):
		n=int(input("Dame un nuemro para la lista 1: "))
		x1.append(n)
	for i in range (0,5):	
		g=int(input("Dame un numero para la lista 2: "))
		x2.append(g)
		t=t+(x1[i]*x2[i])
	return t
n=mul()
print(n)
