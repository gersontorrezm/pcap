l1 = ['#','###','###','# #','###','###','###','###','###','###']
l2 = ['#','  #','  #','# #','#  ','#  ','  #','# #','# #','# #']
l3 = ['#','###','###','###','###','###','  #','###','###','# #']
l4 = ['#','#  ','  #','  #','  #','# #','  #','# #','  #','# #']
l5 = ['#','###','###','  #','###','###','  #','###','###','###']

numero = int(input('Ingrese su numero: '))
tam = len(str(numero))
numero_str = str(numero) 
resultado=[int(digito) for digito in numero_str]
for i in resultado:
    print(l1[i-1])
    print(l2[i-1])
    print(l3[i-1])
    print(l4[i-1])
    print(l5[i-1])
