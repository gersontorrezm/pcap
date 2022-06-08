# Operaciones entre listas
import random

def op(a,b):
    s = []
    r = []
    m = []
    d = []
    for i in range(len(a)):
        s.append(a[i]+b[i])
        r.append(a[i]-b[i])
        m.append(a[i]*b[i])
        d.append(a[i]/b[i])
    print("La suma es: ",s,"\nLa resta es: ",r,"\nLa multiplicacion es: ",m,"\nLa division es: ",d)
    
l1 = []
l2 = []
for i in range(4):
    l1.append(random.randint(1,10))
    l2.append(random.randint(1,10))

op(l1,l2)
