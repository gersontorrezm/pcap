def agregar_usrs():
    global usrs
    global db
    db = []
    n = int(input("ingrese la cantidad de personas: "))
    for i in range(n):
        x = input("ingrese el nombre: ")
        e = int(input("ingrese la edad: "))
        t = int(input("ingrese la telefono: "))

        usrs = {"nombre":x,
                "edad":e,
                "telefono":t}
        db.append(usrs)
    print("\nRegistrado con éxito")
    for i in db:
        print(i)
        
def buscar_usrs():
    search = input("Ingrese el usuario a buscar: ")
    c = 0
    for i in db:
        if search in i.values():
            c+=1
            print(i)
    if c == 0:
        print(f'El usuario {search} no se encuentra registrado')
    
def mod_usrs():
    id_mod = input("ingrese el usuario que desea modificar: ")
    for i in db:
        if id_mod in i.values():
            key_mod = input(f'''
            ¿Qué paramentro de {id_mod} desea modificar?
            1. nombre
            2. edad
            3. telefono
            ''')
            if key_mod == "1":
                new_name = input("Ingrese el nuevo nombre: ")
                i['nombre'] = new_name            
            elif key_mod == "2":
                new_age = input("Ingrese la nueva edad: ")
                i['edad'] = new_age 
            elif key_mod == "3":
                new_pho = input("Ingrese el nuevo telefono: ")
                i['telefono'] = new_pho 
            else:
                print("Numero incorrecto")
            break
    else:
        print(f"El usuario {id_mod} no se encuentra registrado")

print('''
      ================
         Directorio 
      ================
      ''')

while True:
    print('''
Menu:
1. Registrar
2. Buscar
3. Modificar
4. Salir

''')
    
    m = input("Ingrese la opcion: ")
    if m == "1":
        agregar_usrs()
    elif m =="2":
        buscar_usrs()
    elif m == "3":
        mod_usrs()
    else:
        print("Finalizado")
        break
