from random import randint, choice

fon = '.'
ris = '*'
popal='x'
nepopal='-'

def myprint10(pole):
    print('   ', end='')
    for i in range(10):
        print(i, end='  ')
    print()
    print('   ', end='')
    for i in range(10):
        print(chr(65 + i), end='  ')
    print()
    for i in range(10):
        if i < 9:
            print(i, end='  ')
        else:
            print(i, end='  ')
        for j in range(10):
            print(pole[i][j], end='  ')
        print(i)
    print('   ', end='')
    for i in range(10):
        print(chr(65 + i), end='  ')
    print()
    print('   ', end='')
    for i in range(10):
        print(i, end='  ')
    print()


def proverka(pole, row, col):
    svobodno = True
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if i == row and j == col:
                pass
            else:
                try:
                    if pole[i][j] == ris:
                        svobodno = False
                except IndexError:
                    continue
    return svobodno


def varianty(r, c):
    var = []
    if r - 1 >= 0:
        var.append(str(r - 1) + ',' + str(c))
    if c - 1 >= 0:
        var.append(str(r) + ',' + str(c - 1))
    if r + 1 <= 9:
        var.append(str(r + 1) + ',' + str(c))
    if c + 1 <= 9:
        var.append(str(r) + ',' + str(c + 1))
    return (var)


idletter = []
idnumber = []
for i in range(10):
    idletter.append(chr(65 + i))
    idnumber.append(i + 1)
stroka = [fon] * 10
karta = []
for i in range(10):
    mystr = stroka.copy()
    karta.append(mystr)
# Создали пустое игровое поле
# myprint10(karta)
del stroka
del mystr

# Расставляем однопалубные корабли:
k1 = 0  # однопалубные корабли
while k1 < 4:
    r = randint(0, 9)  # row
    c = randint(0, 9)  # col
    if karta[r][c] == fon:
        # проверяем, нет ли кораблей в округе
        if proverka(karta, r, c):
            karta[r][c] = ris
            k1 += 1
# myprint10(karta)

# Расставляем двухпалубные корабли:
k2 = 0  # Должно быть три двухпалубных корабля
# Случайным образом ставим первую мачту корабля, если место пустое
while k2 < 3:
    r1 = randint(0, 9)  # row
    c1 = randint(0, 9)  # col
    if karta[r1][c1] == fon:
        # Если в округе нет других кораблей, то
        if proverka(karta, r1, c1):
            # создаём поле вариантов, куда можно поставить вторую палубу:
            var = []
            var = varianty(r1, c1)
            # Случайным образом выбираем, куда поставить вторую палубу
            poluchilosb = False
            while not (poluchilosb):
                if len(var) > 0:
                    mesto = choice(var)
                    # print('mesto=',mesto)
                    var.remove(mesto)
                    place = mesto.split(',')
                    # print('place=',place)
                    r2 = int(place[0])
                    c2 = int(place[1])
                    if proverka(karta, r2, c2):
                        karta[r1][c1] = ris
                        karta[r2][c2] = ris
                        poluchilosb = True
                        k2 += 1
                else:
                    break
# Расставляем трёх-палубные корабли - 2 штуки
k3 = 0
while k3 < 2:
    # Случайным образом ставим первую палубу, если место не занято
    r = randint(0, 9)
    c = randint(0, 9)
    if karta[r][c] == fon:
        # Если в округе нет других кораблей, то
        if proverka(karta, r, c):
            # создаём поле вариантов, куда можно поставить вторую палубу:
            var = []
            var = varianty(r, c)
            # Случайным образом выбираем, куда поставить вторую палубу
            poluchilosb1 = False
            while not (poluchilosb1):
                if len(var) > 0:
                    mesto = choice(var)
                    # print('mesto=',mesto)
                    var.remove(mesto)
                    place = mesto.split(',')
                    # print('place=',place)
                    r1 = int(place[0])
                    c1 = int(place[1])
                    if proverka(karta, r1, c1):
                        # Если поставили вторую палубу, то надо ставить третью:
                        # создаём поле вариантов, куда можно поставить третью палубу:
                        var1 = []
                        var1 = varianty(r1, c1)
                        # Проходимся по списку var и удаляем из него варианты r,c
                        fordel=[]
                        for i in range(len(var1)):
                            s = var1[i]
                            mylist = s.split(',')
                            rx = int(mylist[0])
                            cx = int(mylist[1])
                            # print('mylist=',mylist)
                            if rx == r and cx == c:
                                fordel.append(var1[i])
                        if len(fordel)>0:
                            for el in fordel:
                                var1.remove(el)
                        # Теперь var1 хранит те варианты, куда можно поставить третью палубу
                        # Случайным образом выбираем, куда поставить третью палубу:
                        poluchilosb2 = False
                        while not (poluchilosb2):
                            if len(var1) > 0:
                                mesto = choice(var1)
                                # print('mesto=',mesto)
                                var1.remove(mesto)
                                place = mesto.split(',')
                                # print('place=',place)
                                r2 = int(place[0])
                                c2 = int(place[1])
                                if proverka(karta, r2, c2):
                                    karta[r][c] = ris
                                    karta[r1][c1] = ris
                                    karta[r2][c2] = ris
                                    poluchilosb1 = True
                                    poluchilosb2 = True
                                    k3 += 1
                            else:
                                break
# Расставляем 1 четырехпалубный корабль
k4 = 0
while k4 < 1:
    # Случайным образом ставим первую палубу, если место не занято
    r = randint(0, 9)  # row
    c = randint(0, 9)  # col
    if karta[r][c] == fon:
        # Если в округе нет других кораблей, то
        if proverka(karta, r, c):
            # создаём поле вариантов, куда можно поставить вторую палубу:
            var = []
            var = varianty(r, c)
            # Случайным образом выбираем, куда поставить вторую палубу
            poluchilosb1 = False
            while not (poluchilosb1):
                if len(var) > 0:
                    mesto = choice(var)
                    # print('mesto=',mesto)
                    var.remove(mesto)
                    place = mesto.split(',')
                    # print('place=',place)
                    r1 = int(place[0])
                    c1 = int(place[1])
                    if proverka(karta, r1, c1):
                        # Если поставили вторую палубу, то надо ставить третью:
                        # создаём поле вариантов, куда можно поставить третью палубу:
                        var1 = []
                        var1 = varianty(r1, c1)
                        # Проходимся по списку var1 и удаляем из него варианты r,c
                        fordel=[]
                        for i in range(len(var1)):
                            s = var1[i]
                            mylist = s.split(',')
                            rx = int(mylist[0])
                            cx = int(mylist[1])
                            # print('mylist=',mylist)
                            if rx == r and cx == c:
                                fordel.append(var1[i])
                        if len(fordel)>0:
                            for el in fordel:
                                var1.remove(el)
                        # Теперь var1 хранит те варианты, куда можно поставить третью палубу
                        # Случайным образом выбираем, куда поставить третью палубу:
                        poluchilosb2 = False
                        while not (poluchilosb2):
                            if len(var1) > 0:
                                mesto = choice(var1)
                                # print('mesto=',mesto)
                                var1.remove(mesto)
                                place = mesto.split(',')
                                # print('place=',place)
                                r2 = int(place[0])
                                c2 = int(place[1])
                                if proverka(karta, r2, c2):
                                    # Если поставили третью палубу, то надо ставить четвертую:
                                    # создаём поле вариантов, куда можно поставить четвёртую палубу:
                                    var2 = []
                                    var2 = varianty(r2, c2)
                                    # Проходимся по списку var2 и удаляем из него варианты r,c и r1,c1
                                    fordel=[]
                                    for i in range(len(var2)):
                                        s = var2[i]
                                        mylist = s.split(',')
                                        rx = int(mylist[0])
                                        cx = int(mylist[1])
                                        # print('mylist=',mylist)
                                        if rx == r and cx == c:
                                            fordel.append(var2[i])
                                        elif rx == r1 and cx == c1:
                                            fordel.append(var2[i])
                                    if len(fordel)>0:
                                        for el in fordel:
                                            var2.remove(el)

                                    # Теперь var2 хранит те варианты, куда можно поставить третью палубу
                                    # Случайным образом выбираем, куда поставить третью палубу:
                                    poluchilosb3 = False
                                    while not (poluchilosb3):
                                        if len(var2) > 0:
                                            mesto = choice(var2)
                                            # print('mesto=',mesto)
                                            var2.remove(mesto)
                                            place = mesto.split(',')
                                            # print('place=',place)
                                            r3 = int(place[0])
                                            c3 = int(place[1])
                                            if proverka(karta, r3, c3):
                                                karta[r][c] = ris
                                                karta[r1][c1] = ris
                                                karta[r2][c2] = ris
                                                karta[r3][c3] = ris
                                                poluchilosb1 = True
                                                poluchilosb2 = True
                                                poluchilosb3 = True
                                                k4 += 1
                                        else:
                                            break
                            else:
                                break
                else:
                    break

#myprint10(karta)
print('Привет! Давай сыграем в морской бой!')
myvar=[]
for i in range(10):
    for j in range(10):
        myvar.append(str(i)+','+str(j))
stroka = [fon] * 10
yourkarta = []
for i in range(10):
    mystr = stroka.copy()
    yourkarta.append(mystr)

del stroka
del mystr
#print(myvar)
mypopal=0
yourpopal=0
gameon=True
while gameon:
    yourturn=True
    while yourturn:
        ur=int(input('Твой ход: \nСтрока (0-9): '))
        uc=int(input('Столбец (0-9): '))
        if karta[ur][uc]==fon:
            print('Мимо!')
            karta[ur][uc]=nepopal
            yourturn=False
        elif karta[ur][uc]==ris:
            print('Попал!')
            karta[ur][uc]=popal
            yourpopal+=1
            if yourpopal==20:
                print('Ты победил!!! :)))')
                yourturn=False
                gameon=False
                myturn=False
                break
        elif karta[ur][uc]!=fon:
            print('Этот ход уже был!')
    if gameon:
        myturn=True
    while myturn:
        myvariant=choice(myvar)
        myvar.remove(myvariant)
        print('Мой ход:')
        mr=int(myvariant[0])
        mc=int(myvariant[-1])
        print('Строка: ',mr)
        print('Столбец: ',mc)
        otvet=input('Попал? да или нет: ')
        if otvet=='да':
            yourkarta[mr][mc]=popal
            mypopal+=1
            if mypopal==20:
                print('Я победил! :)')
                myturn=False
                yourturn=False
                gameon=False
                break
        elif otvet=='нет':
            yourkarta[mr][mc]=nepopal
            myturn=False
            
myprint10(karta)
