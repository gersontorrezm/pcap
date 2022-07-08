print('''
CIFRADO
''')
txt = input('ingrese un texto a cifrar: ').lower()
s = int(input('Ingrese un numero de salto: '))
c = ''
d = ''
for i in txt:
    n = ord(i)+s
    if n > 122:
        n = n - 26 
    c += chr(n)
print('El texto cifrado es: ',c)

for i in c:
    n = ord(i)-s
    if n < 97:
        n += 1
    d += chr(n)
print('El texto descifrado es: ',d)
