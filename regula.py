from math import exp 

def fonk(i):
    return exp(i)-2
    
def f(a,b):
	x = (a*fonk(b)-b*fonk(a))/(fonk(b)-fonk(a))
	return x    
    
def regula_falsi(a,b,hata,sinir=100000):
	a = float(a)
	b = float(b)
	sayac = 0
	xa=99
	if(fonk(a) == 0):
		print a
		return
	elif(fonk(b) == 0):
		print b
		return
	elif(fonk(a)*fonk(b)<0):
		while (sayac < sinir):
			x0=f(a,b)
			if (abs(x0-xa)>hata):
				break
			if(fonk(a)*fonk(x0)<0):
				b=x0
			elif(fonk(x0)*fonk(b)<0):
				a=x0	
			else:
				print x0
				return
			xa=x0	 
			sayac+=1
	print x0	

regula_falsi(0,1,0)	
