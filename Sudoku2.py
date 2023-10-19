import random
popytok=0
sudoku = [0] * 9
s = []
for i in range(9):
    sud = sudoku.copy()
    s.append(sud)


def prints(a):
    print(' | ', end='')
    for i in range(9):
        if (i + 1) % 3 == 0:
            print(i + 1, end='| ')
        else:
            print(i + 1, end='  ')
    print()
    print('-' * 28)
    for i in range(9):
        print(i + 1, end='| ')
        for j in range(9):
            if (j + 1) % 3 == 0:
                print(a[i][j], end='| ')
            else:
                print(a[i][j], end='  ')
        print()
        if (i + 1) % 3 == 0:
            print('-' * 28)


# prints(s)
# Расставляем единицы
# Создаём список координат, в которых можно поставить единицы
sudoku = [0] * 9
koord = []
for i in range(9):
    sud = sudoku.copy()
    koord.append(sud)
noshibok = 0
poluchilosb = False
while not (poluchilosb):
    noshibok=0
    for i in range(9):
        for j in range(9):
            s[i][j] = 0
    #prints(s)
    #print('получилось=',poluchilosb)
    cifra = 1
    while cifra < 10:  # цифра
        #print('cifra=',cifra)
        #print('noshibok',noshibok)
        if noshibok == 81:
            break
        noshibok = 0
        for i in range(9):
            for j in range(9):
                koord[i][j] = 0
        r1var = []
        c1var = []
        for i in range(9):
            r1var.append(i)
            c1var.append(i)
        n1 = 0
        while n1 < 9:
            # print('n1=',n1)
            r1 = random.choice(r1var)
            c1 = random.choice(c1var)
            #print('r1=',r1,'c1=',c1)
            #print('koord[r1][c1]=',koord[r1][c1])
            #print('s[r1][c1]=',s[r1][c1])
            if koord[r1][c1] == 0 and s[r1][c1] == 0:
                s[r1][c1] = cifra
                r1var.remove(r1)
                c1var.remove(c1)
                #print('r1=',r1)
                #print('c1=',c1)
                # Строку и столбец помечаем как занятые:
                for i in range(9):
                    koord[r1][i] = cifra
                    koord[i][c1] = cifra
                # Выбранный квадрат помечаем как занятый:
                # Определяем кординаты квадрата:
                rkvadrat = r1 // 3
                ckvadrat = c1 // 3
                for i in range(9):
                    for j in range(9):
                        if i // 3 == rkvadrat and j // 3 == ckvadrat:
                            koord[i][j] = cifra
                n1 += 1
                #print('sudoku=')
                #prints(s)
                #print('koord=')
                #prints(koord)
                if cifra==9 and n1==9:
                    poluchilosb = True
            else:
                noshibok += 1
                if noshibok >= 81:
                    #print('Всё с начала')
                    #prints(s)
                    #print(cifra)
                    n1 = 9
                    poluchilosb = False
                    popytok+=1
        cifra += 1
print()
prints(s)
print('Попыток=',popytok)
