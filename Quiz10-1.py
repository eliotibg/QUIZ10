def l():
	j=[]
	f=[]
	t=0
	for i in range (0,10):
		n=int(input(" Dame un numero para la lista: "))
		j.append(n)
	for i in range (0,10):
		c=j[i]%3
		if(c==0):
			s=j[i]
			f.append(s)
			t=t+j[i]
	print(f)
	return t

n=l()
print(n)