db = []
for i in range(3):
    n = input("ingrese su nombre: ")
    e = int(input("ingrese su edad: "))
    t = int(input("ingrese su telefono: "))
    
    usrs = {"nombre":n,
            "edad":e,
            "telefono":t}
    db.append(usrs)
    
for i in db:
    print(i)
