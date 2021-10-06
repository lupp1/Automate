#Tic-Tac-Toe Game
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
def printBoard(board):
    print(f"{board['top-L']}|{board['top-M']}|{board['top-R']}")
    print('-+-+-')
    print(f"{board['mid-L']}|{board['mid-M']}|{board['mid-R']}")
    print('-+-+-')
    print(f"{board['low-L']}|{board['low-M']}|{board['low-R']}")
turn = 'X'
def playerMove():
    for i in range(9):
        global turn
        printBoard ( theBoard )
        print(f'Vez de {turn}. Mover em qual espaço?')
        move = input('Escolha dentre top-L, mid-M, etc:')
        theBoard[move] = turn
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
playerMove()
