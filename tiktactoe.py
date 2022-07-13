import random

def DisplayBoard(board):
    # La función acepta un parámetro el cual contiene el estado actual del tablero
    # y lo muestra en la consola.
    j = 0
    for i in board:
        print('+-----------------+')
        print('| ',i[j],' | ',i[j+1],' | ',i[j+2],' |')    

def EnterMove(board):
    # La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento, 
    # verifica la entrada y actualiza el tablero acorde a la decisión del usuario.
    p = int(input('Ingresa tu movimiento: '))
    c = 1
    for i in range(3):
        for j in range(3):
            if p == c and board[i][j] != 'x' and board[i][j] != 'o':
                board[i][j] = 'o'
            c += 1  
    
def MakeListOfFreeFields(board):
    # La función examina el tablero y construye una lista de todos los cuadros vacíos.
    # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.
    vacios = []
    for i in range(3):
        for j in range(3):
            if board[i][j] != 'x' and board[i][j] != 'o':
                v = (i,j)
                vacios.append(v)
    return vacios
    

def VictoryFor(board, sign):
    # La función analiza el estatus del tablero para verificar si
    # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.
    global sw
    ganador = [[sign, sign, sign], [sign, sign, sign], [sign, sign, sign]]
    ganador1 = [ganador[0][0], ganador[1][1], ganador[2][2]]
    ganador2 = [ganador[2][0], ganador[1][1], ganador[0][2]]
    ganadorv3 = [ganador[0][0], ganador[0][1], ganador[0][2]]
    board1 = [board[0][0], board[1][1], board[2][2]]
    board2 = [board[2][0], board[1][1], board[0][2]]
    boardv3 = [board[0][0], board[1][0], board[2][0]]
    boardv4 = [board[0][1], board[1][1], board[2][1]]
    boardv5 = [board[0][2], board[1][2], board[2][2]]
                
    if board[0] == ganador[0]:
        if sign == 'o':
            print('*** G A N A S T E ***')
        else:
            print('*** T E  G A N É ***')
        sw = 0
    if board[1] == ganador[1]:
        if sign == 'o':
            print('*** G A N A S T E ***')
        else:
            print('*** T E  G A N É ***')
        sw = 0
    if board[2] == ganador[2]:
        if sign == 'o':
            print('*** G A N A S T E ***')
        else:
            print('*** T E  G A N É ***')
        sw = 0
    if board1 == ganador1:
        if sign == 'o':
            print('*** G A N A S T E ***')
        else:
            print('*** T E  G A N É ***')
        sw = 0
    if board2 == ganador2:
        if sign == 'o':
            print('*** G A N A S T E ***')
        else:
            print('*** T E  G A N É ***')  
        sw = 0
    if ganadorv3 == boardv3:
        if sign == 'o':
            print('*** G A N A S T E ***')
        else:
            print('*** T E  G A N É ***')  
        sw = 0
    if ganadorv3 == boardv4:
        if sign == 'o':
            print('*** G A N A S T E ***')
        else:
            print('*** T E  G A N É ***')  
        sw = 0
    if ganadorv3 == boardv5:
        if sign == 'o':
            print('*** G A N A S T E ***')
        else:
            print('*** T E  G A N É ***')  
        sw = 0
    
def DrawMove(board):
    # La función dibuja el movimiento de la máquina y actualiza el tablero.
    try:
        vacios = MakeListOfFreeFields(board)
        ran = random.choice(vacios)
        if len(ran) > 0:

            board[ran[0]][ran[1]] = 'x'
        else:
            print('juego terminado')
    except:
        print('Empate....')


board = [
    [1,2,3],
    [4,'x',6],
    [7,8,9]
]

sw = 1
mov = 0

print('''

I N I C I A N D O 
E L 
J U E G O........

''')

DisplayBoard(board)

while sw == 1:
    mov += 1
    if mov > 4:
        print('____E M P A T E____')
        break
    EnterMove(board) #movimiento jugador
    VictoryFor(board, 'o') #verifica si hay ganador
    DrawMove(board) #movimiento maquina
    DisplayBoard(board)
    if sw == 1:
        VictoryFor(board, 'x') #verifica si hay ganador
