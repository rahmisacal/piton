from math import exp

def fonk(i):
    return exp(i)-2

def yarilama(a,b):
    a = float(a)
    b = float(b)
    f1=fonk(a)
    f2=fonk(b)
    if f1 == 0:
        print a
    elif f2 == 0:
        print b
    elif f1*f2<0:
        c = (a+b)/2
        f3 = fonk(c)
        if f1*f3<0:
            yarilama(a,c)
        elif f2*f3<0:
            yarilama(b,c)
        elif f3 == 0:
            print c
    else:
        print "Kök aralığın dışındadır."

        

    
