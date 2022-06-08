# Operaciones entre listas
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
    

l1 = [2,4,6,8]
l2 = [8,6,4,2]

op(l1,l2)
