import getpass
from datetime import date

#Validamos credenciales
def verifyCredentials(usr, psw):
    users = {
        'admin':'admin',
        'gerson':'1996',
        'guest':'guest'
    }
    if usr in users.keys():
        if users[usr] == psw:
            return True
        else:
            print('\nContraseña incorrecta')
            return False
    else:
        print('\nUsuario incorrecto')

        
#Mostramos Menú
def messageM():
    print('''
     _   _   ____   _     _   _    _
    | \_/ | |  __| | \   | | | |  | |
    |     | | |__  |  \  | | | |  | |
    | \_/ | |  __| | \ \ | | | |  | |
    | | | | | |__  | |\ \| | | |__| |
    |_| |_| |____| |_| \___| |______|
    Sistema de ventas
    1 : Inventario.
    2 : Agregar productos.
    3 : Quitar productos.
    4 : Facturación.
    ''')

#Mostramos productos:
def products(dic_products):
    
    print('\nID  PRODUCTO  PRECIO  CANTIDAD')
    for keys in dic_products.keys():
        print(keys,':', dic_products[keys][0],', ', dic_products[keys][2],', ', dic_products[keys][3])
    return dic_products
 
#Agregamos un producto:
def addProduct(dic_products):
    try:
        id_product = int(input('Ingrese el ID: '))
        product = input('Ingrese el nombre del producto: ')
        category = input('Ingrese la categoría: ')
        price = int(input('Ingrese el precio: '))
        quant = int(input('Ingrese la cantidad: '))
        dic_products.update({id_product : [product, category, price, quant]})
        products(dic_products)
    except ValueError:
        print('Ingrese un numero en precio y cantidad')
    except:
        print('Error...')

#Eliminamos un producto:
def delProduct(dic_products):
    try:
        products(dic_products)
        id_product = int(input('Ingrese el ID del producto a eliminar: '))
        del_product = dic_products[id_product][0]
        del dic_products[id_product]
        products(dic_products)
        print(f'\nSe eliminó el producto: {del_product}')
    except:
        print(f'No existe ID: {id_product}')
 

#Imprimimos la factura
def sales(dic_products):
    try:
        print('Facturación:')
        name = input('Nombre de cliente')
        nit = int(input('Nit: '))
        date1 = date.today()
        id_product = int(input('Ingrese el ID: '))
        dic_products[id_product][3] = dic_products[id_product][3]-1
        print(f'''
        =======================
             F A C T U R A

        CLIENTE:   {name}
        NIT:       {nit}
        FECHA:     {date1}
        PRODUCTO:  {dic_products[id_product][0]}
        PRECIO:    {dic_products[id_product][2]}

        ========================

        ''')
        return dic_products
    except:
        print('\nNo existe el producto')
    
dic_products = {
        #ID   prod.  cat.    precio  cantidad 
        1 : ['xbox','consola',2000,10],
        2 : ['ps4','consola',3000,900],
        3 : ['ps5','consola',5000,600],
        4 : ['switch','consola',2600,200],
        5 : ['switch oled','consola',3400,1000],
    }    


while True:
    usr = input('Ingrese su usuario: ')
    psw = getpass.getpass('Ingrese su contraseña: ')
    if verifyCredentials(usr, psw):
        print('\nAcceso correcto.')
        messageM()
        break
    
while verifyCredentials(usr, psw):
    
    menu = input('Ingrese la opción: ')
    if menu == '1':
        products(dic_products)
        menu2 = input('\n¿Desea volver al menú? y/n ').lower()
        if menu2 == 'y':
            messageM()
        else:
            print('Saliendo...')
            break        
    elif menu == '2':
        addProduct(dic_products)
        menu2 = input('\n¿Desea volver al menú? y/n ').lower()
        if menu2 == 'y':
            messageM()
        else:
            print('Saliendo...')
            break
    elif menu == '3':
        delProduct(dic_products)
        menu2 = input('\n¿Desea volver al menú? y/n ').lower()
        if menu2 == 'y':
            messageM()
        else:
            print('Saliendo...')
            break
    elif menu == '4':
        sales(dic_products)
        menu2 = input('\n¿Desea volver al menú? y/n ').lower()
        if menu2 == 'y':
            messageM()
        else:
            print('Saliendo...')
            break
    
