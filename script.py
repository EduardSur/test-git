M = [[' ', '1', '2', '3'],
     ['1', '-', '-', '-'],
     ['2', '-', '-', '-'],
     ['3', '-', '-', '-']]
n = 0
def view():
    for i in range(4):
        print(M[i][0],M[i][1],M[i][2],M[i][3])
    return None

def Hod():
    while True:
        str_x = input('Введи Х от 1 до 3')
        str_y = input('Введи У от 1 до 3')
        if str_x in ('1','2','3') and str_y in ('1','2','3'):
            x=int(str_x)
            y=int(str_y)
            if M[x][y] == '-':
                break
            print('\nЯчейка занята, введите другие координаты\n')
            view()
        else:
            print('\nНеправильные координаты! Попробуйте еще раз.\n')
            view()
    if n%2 == 0:
        M[x][y] = 'O'
    else:
        M[x][y] = 'X'
    return None

def Proverka():
    x = False
    o = False
    if (M[1][1] == 'X' and M[1][2] == 'X' and M[1][3] == 'X') or (M[2][1] == 'X' and M[2][2] == 'X' and M[2][3] == 'X') or (M[3][1] == 'X' and M[3][2] == 'X' and M[3][3] == 'X') or (M[1][1] == 'X' and M[2][1] == 'X' and M[3][1] == 'X') or (M[1][2] == 'X' and M[2][2] == 'X' and M[3][2] == 'X') or (M[1][3] == 'X' and M[2][3] == 'X' and M[3][3] == 'X') or (M[1][1] == 'X' and M[2][2] == 'X' and M[3][3] == 'X') or (M[1][3] == 'X' and M[2][2] == 'X' and M[3][1] == 'X'):
        x = True
    if (M[1][1] == 'O' and M[1][2] == 'O' and M[1][3] == 'O') or (M[2][1] == 'O' and M[2][2] == 'O' and M[2][3] == 'O') or (M[3][1] == 'O' and M[3][2] == 'O' and M[3][3] == 'O') or (M[1][1] == 'O' and M[2][1] == 'O' and M[3][1] == 'O') or (M[1][2] == 'O' and M[2][2] == 'O' and M[3][2] == 'O') or (M[1][3] == 'O' and M[2][3] == 'O' and M[3][3] == 'O') or (M[1][1] == 'O' and M[2][2] == 'O' and M[3][3] == 'O') or (M[1][3] == 'O' and M[2][2] == 'O' and M[3][1] == 'O'):
        o = True
    if x:
        return print('\n---Выиграл Х---')
    if o:
        return print('\n---Выиграл O---')
    return True

view()
print('\n-------------\n')
while True:
    n +=1
    Hod()
    print('\n-------------\n')
    view()
    win=Proverka()
    if not win:
        break
    if n == 9:
        print('\n-----Ничья-----\n')
        break
    print('\n-------------\n')