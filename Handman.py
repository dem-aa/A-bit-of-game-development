import random

images = [
    '''

    |____
    |
    |
    |
    | 
    |\\
    | \\
    =======

    ''',
    '''

    |____
    |   |
    |
    |
    |
    |\\
    | \\
    =======

    ''',
    '''

    |____
    |   |
    |   o
    |  
    | 
    |\\
    | \\
    =======

    ''',
    '''

    |____
    |   |
    |   o
    |   |
    |  
    |\\
    | \\
    =======

    ''',
    '''

    |____
    |   |
    |   o
    |  /|
    |  
    |\\
    | \\
    =======

    ''',
    '''

    |____
    |   |
    |   o
    |  /|\\
    |  
    |\\
    | \\
    =======

    ''',
    '''

    |____
    |   |
    |   o
    |  /|\\
    |  /
    |\\
    | \\
    =======

    ''',
    '''

    |____
    |   |
    |   o
    |  /|\\
    |  / \\
    |\\
    | \\
    =======

    '''
]

WORDS = {
    'фрукты' : [
        ['апельсин', 'цитрус'],
        ['манго','может цитрус, а может и нет)'],
        ['грейпфрут', 'цитрус побольше, чем просто цитрус'],
        ['ананас','ваще большой цитрус'],
        ['мандарин','маленький цитрус']
        ],
    'животные' : [
        ['жираф', 'современный диплодок'],
        ['бегемот', 'Мото-мото'],
        ['кошка', 'не приматывайте бутерброд с маслом на спину'],
        ['ящерица', 'змея, но с ногами'],
        ['змея', 'ящерица, но без ног'],
        ],
    'космос' : [
        ['звезда', 'такая в небе'],
        ['галактика', 'так звёздный крейсер назывался'],
        ['орбита', 'лагерь в котором была КЛШ в 2022'],
        ['спутник', 'остановка в Крск'],
        ['ракета', 'Я - ..., я - ..., полетела в космос']
        ],
    'интерьер' : [
        ['комод', 'типо тумбочка'],
        ['столешница', 'она на кухне рядом с плитой'],
        ['дизайн', 'обстановка комнаты'],
        ['тумбочка', 'маленький шкаф'],
        ['столик', 'кофейный']
        ],
    'клш' : [
        ['зондер', 'в ночи от него не уйти'],
        ['ламзинарий', 'там Серёжа'],
        ['пасадобль', 'дирижабль'],
        ['уховёртка', 'коловратка'],
        ['коловратка', 'уховёртка']
        ]
}

Rate = {
    'Победы' : 0,
    'Поражения' : 0
}

def menu():

    MENU =  '[1] Начать новую игру \n'\
            '[2] Выход из игры'

    CHOICE = '[1] Случайная категория \n'\
             '[2] Фрукты \n'\
             '[3] Животные\n'\
             '[4] Космос \n'\
             '[5] Интерьер \n'\
             '[6] КЛШ'

    print()
    print(MENU)
    print()
    first_user_choice = input('>>> ')

    if first_user_choice == '1':
        print()
        print(CHOICE)
        print()
        second_user_choice = input('>>> ')
        if second_user_choice in "123456789":
            second_user_choice  = int(second_user_choice) - 2
            game(second_user_choice)
        else:
            print('Ошибка! Серьёзно? Там всего три варианта!')
    elif first_user_choice == '2':
        return 0
    else:
        print('Ошибка! Читать учись, неуч')

def guess_word(second_user_choice):
    '''
    1. Выбор темы
    2. Выбор слова
    '''
    categories = list(WORDS.keys())

    if second_user_choice == -1:
        category = random.choice(categories)
    else:
        category = categories[second_user_choice]

    quest_word_and_ambulance = random.choice(WORDS[category])
    quest_word = quest_word_and_ambulance[0]
    ambulance = quest_word_and_ambulance[1]
    category = category.upper()
    quest_word = quest_word.upper()
    return category, quest_word, ambulance

def user_guess(answer, recent_letters):
    '''
    1. Ничего не принимает
    2. Цикл:
        [1] Считывает символ
        [2] Проверяет, что: 
            1) Введён только 1 символ
            2) Это буква русского алфавита 
    3. Возвращает букву
    '''

    RU = 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ'

    while True:
        print('Введите букву:')
        letter = input('>>> ').upper()
        if len(letter) != 1:
            print('Ошибка. Введите ОДИН символ!')
            continue
        if letter not in RU:
            print('Ошибка. Введите букву русского языка!')
            continue
        if letter in answer or letter in recent_letters:
            print('Ошибка. Буква уже была введена!')
            continue
        break
    return letter

def game(second_user_choice):

    '''
    Сама, собственно, игра
    '''
    category, quest_word, ambulance = guess_word(second_user_choice)

    answer = '-' * len(quest_word)

    recent_letters = ''

    mistakes = 0
    print(images[mistakes])

    while mistakes < 7 and answer != quest_word:
        print('Загаданное слово:', answer)
        print('Тема:', category)
        print('Допущено ошибок:', mistakes, 'из 7')

        letter = user_guess(answer, recent_letters)
        
        if letter in quest_word:
            for i in range(len(quest_word)):
                if letter == quest_word[i]:
                    answer = answer[:i] + letter + answer[i+1:]
            print('Крутой! Угадал!')
        else:
            print('Эх... А вот и не угадал...')
            mistakes += 1
            recent_letters += letter
        
        print(images[mistakes])

        if mistakes >= 3:
            print('Подсказка:', ambulance)

    if mistakes == 7:
        print('Game over')
        print('Загаданное слово:', quest_word)
        Rate['Поражения'] += 1
    else:
        print('Супер мега крут! Или супер мега крутая!')
        print('Загаданное слово:', quest_word)
        Rate['Победы'] += 1
        
    print()
    for key, value in Rate.items():
        print(key, value)

    menu()

menu()

# Допилить с выбором слов
