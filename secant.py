from math import exp

def f(i):
    return exp(i)-2
    
def f_u(i):
	return exp(i)
	
def newton(ilklendir,hata):
	x0 = ilklendir
	x1 = x0-(f(x0)/f_u(x0))
	
	while (abs(f(x1)-f(x0))>hata):
	#~ while (abs(f(x1)-f(x0))>hata*f(x0)):
		x0=x1
		x1=x1-(f(x1)/f_u(x1))
	
	print x1
	
newton(10,0.001)			       
