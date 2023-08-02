import random

# r = input()
# mas = ['Ножницы','Камень','Бумага']
# random.shuffle(mas)

# q =mas[0]

# if q == r:
#     print('Ничья , компьютер выбрал' , q)

# elif q == 'Ножницы' and r == 'Бумага' or q == 'Камень' and r =='Ножницы'  or q == 'Бумага' and r =='Камень':
#     print('Вы проиграли , компьютер выбрал' , q)


# elif q == 'Ножницы' and r == 'Камень' or q == 'Камень' and r =='Бумага'  or q == 'Бумага' and r =='Ножницы':
#     print('Вы выиграли , компьютер выбрал' , q)
# else:
#     print('Пожалуйста напишите Ножницы, Камень или Бумага')

mas = []
rand = random.randint(2,11)
if rand == 5:
        rand = random.randint(2,11)
you = rand
mas.append(rand)

print (mas)



rand = random.randint(2,11)
if rand == 5:
        rand = random.randint(2,11)
dil = rand


while True:
    pass_more = input('Хватит или Еще? ')
    if pass_more == 'Еще':
        rand = random.randint(2,11)
        if rand == 5:
            rand = random.randint(2,11)
        you += rand
        mas.append(rand)
        print (mas)
        # last = rand
        rand = random.randint(2,11)
        if rand == 5:
            rand = random.randint(2,11)
        dil += rand
    elif pass_more == 'Хватит':
        break

    if you > 21:
        print (f'Ваши очки {you}')
        print (f'Очки дилера {dil}')
        print('not win')
        break

    if dil > 21:
        print (f'Ваши очки {you}')
        print (f'Очки дилера {dil}')
        print('win')
        break

        
if pass_more == 'Хватит':
    print (f'Ваши очки {you}')
    print (f'Очки дилера {dil}')

    if you > dil :
        print('win')
    else:
        print('not win')



with open('tex.txt','a',encoding='utf-8') as file:
    if you > dil :
        print(file.write(f'Вы выйграли со счетом {you}:{dil}'+ '\n'))
    else:
        print(file.write(f'Компьютер выйграл со счетом {dil}:{you}'+ '\n'))





