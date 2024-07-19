M = [[' ', '1', '2', '3'],
     ['1', '-', '-', '-'],
     ['2', '-', '-', '-'],
     ['3', '-', '-', '-']]
n = 0
def view():
    for i in range(4):
        print(M[i][0],M[i][1],M[i][2],M[i][3])
    return None

def Hod(n):
    while True:
        x = int(input('Введи Х'))
        y = int(input('Введи У'))
        if M[x][y] == '-':
            break
        print('Ячейка занята, введите другие координаты')
    if n == 0:
        M[x][y]='X'
        n = 1
    else:
        M[x][y] = 'O'
        n = 0
    return n

def Proverka():
    x = False
    o = False
    if (M[1][1] == 'X' and M[1][2] == 'X' and M[1][3] == 'X') or (M[2][1] == 'X' and M[2][2] == 'X' and M[2][3] == 'X') or (M[3][1] == 'X' and M[3][2] == 'X' and M[3][3] == 'X') or (M[1][1] == 'X' and M[2][1] == 'X' and M[3][1] == 'X') or (M[1][2] == 'X' and M[2][2] == 'X' and M[3][2] == 'X') or (M[1][3] == 'X' and M[2][3] == 'X' and M[3][3] == 'X') or (M[1][1] == 'X' and M[2][2] == 'X' and M[3][3] == 'X') or (M[1][3] == 'X' and M[2][2] == 'X' and M[3][1] == 'X'):
        x = True
    if (M[1][1] == 'O' and M[1][2] == 'O' and M[1][3] == 'O') or (M[2][1] == 'O' and M[2][2] == 'O' and M[2][3] == 'O') or (M[3][1] == 'O' and M[3][2] == 'O' and M[3][3] == 'O') or (M[1][1] == 'O' and M[2][1] == 'O' and M[3][1] == 'O') or (M[1][2] == 'O' and M[2][2] == 'O' and M[3][2] == 'O') or (M[1][3] == 'O' and M[2][3] == 'O' and M[3][3] == 'O') or (M[1][1] == 'O' and M[2][2] == 'O' and M[3][3] == 'O') or (M[1][3] == 'O' and M[2][2] == 'O' and M[3][1] == 'O'):
        o = True
    if x and o:
        return print('Ничья')
    elif x:
        return print('Выиграл Х')
    elif o:
        return print('Выиграл O')
    return True

while True:
    n = Hod(n)
    view()
    if n == 0:
        if not Proverka():
            break
