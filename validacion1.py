def validarUsuario(user):
    if len(user) >= 8:
        return True
    else:
        return False
    
def validarCon(psw):
    num = 0
    let = 0
    if len(psw) >= 8 and len(psw) < 13:
        for i in psw:
            if i.isalpha():
                let += 1
            if i.isdigit():
                num += 1
        if num > 0 and let > 0:
            return True
    else:
        return False
    
user = input('Ingrese su usuario: ')
if validarUsuario(user):
    print('Nombre de usuario aceptable')
    psw = input('Ingrese su contraseña: ')
    if validarCon(psw):        
        print('La contraseña es aceptable')
    else:
        print('La contraseña debe tener al menos 8 caracteres y no más de 12, ademas de numeros y letras.')
else:
    print('El nombre de usuario debe tener al menos 8 caracteres')
