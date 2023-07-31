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


rand = random.randint(2,11)
if rand == 5:
        rand = random.randint(2,11)
you = rand

print (you)


# 


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
        print (you)
        # last = rand
        rand = random.randint(2,11)
        if rand == 5:
            rand = random.randint(2,11)
        dil += rand
    elif pass_more == 'Хватит':
        break

    if you > 21:
        print('not win')
        break

    if dil > 21:
        print('win')
        break

        
if pass_more == 'Хватит':
    print (f'Ваши очки {you}')
    print (f'Очки дилера {dil}')

    if you > dil :
        print('win')
    else:
        print('not win')
        

 





