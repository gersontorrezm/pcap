def mysplit(string):
    lista = []
    word = ''
    for i in string:
        if i != ' ':
            word += i
        else:
            lista.append(word)
            word = ''
    print(lista)
    
print(mysplit('Hola como estas'))
