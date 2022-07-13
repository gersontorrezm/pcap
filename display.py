l1 = ['#','###','###','# #','###','###','###','###','###','###']
l2 = ['#','  #','  #','# #','#  ','#  ','  #','# #','# #','# #']
l3 = ['#','###','###','###','###','###','  #','###','###','# #']
l4 = ['#','#  ','  #','  #','  #','# #','  #','# #','  #','# #']
l5 = ['#','###','###','  #','###','###','  #','###','###','###']

numero = int(input('Ingrese su numero: '))
tam = len(str(numero))
numero_str = str(numero) 
resultado=[int(digito) for digito in numero_str]
display1 = []
display2 = []
display3 = []
display4 = []
display5 = []

for i in resultado:
    display1.append(l1[i-1])
    display2.append(l2[i-1])
    display3.append(l3[i-1])
    display4.append(l4[i-1])
    display5.append(l5[i-1])

print(display1)
print(display2)
print(display3)
print(display4)
print(display5)   
