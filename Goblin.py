import random


def gen_goblin():
    '''
    1. Функция ничего не принимает
    2. Случайные имена, хп, атака, шанс крита, множитель крита
    3. Возращает гоблина
    '''
    goblin = {}
    NAMES = [
        'Таг', 'Хоттабыч', 'Шмяк', 'Кусатыч', 'Плевок', 'Агбалин',
        'Флейкцих', 'Гога', 'Рокобар', 'Громмаш', 'Агбалин', 'Нилбог'
    ]
    goblin['name'] = random.choice(NAMES)
    goblin['hp'] = random.randint(20, 40) * 10
    goblin['hp_max'] = goblin['hp']
    goblin['dmg'] = random.randint(12, 20)
    goblin['crit_chance'] = random.randint(5, 15)
    goblin['crit_mult'] = 2
    return goblin


def attack(attacker, defender):
    '''
    1. Функция принимает атакующего и защищающегося гоблина
    2. Атакующий атакует защищающегося
    3. Возвращает параметры защищающегося гоблина
    '''
    
    dice = random.randint(1, 6)
    attacker_dmg = attacker['dmg'] + dice

    crit = random.randint(1, 100)
    if crit >= 100 - attacker['crit_chance']:
        attacker_dmg = attacker_dmg * attacker['crit_mult']
        print('Крит!!!')

    defender['hp'] = defender['hp'] - attacker_dmg
    print(attacker['name'], "атакует", defender['name'], "с силой", attacker_dmg)
    print("У", defender['name'], "остаётся", defender['hp'])
    return defender


def fight(hero, goblin):
    '''
    1. Получает героя и гоблина
    2. Возвращает героя
    '''
    turn = 0

    while hero['hp'] > 0 and goblin['hp'] > 0:
        turn += 1
        print('Раунд', turn)
        goblin = attack(hero, goblin)

        if goblin['hp'] > 0:
            hero = attack(goblin, hero)
        print()

    if hero['hp'] <= 0:
        print(goblin['name'], 'победил')
    else:
        print(hero['name'], 'победил')

    return hero

def shop(hero):
    '''
    1. Получает героя
    2. Магазин
    3. Возвращает героя
    '''
    MENU = '1 - +10 хп \n'\
           '2 - +2 атаки \n'\
           '3 - +3% шанса крита'
    print(MENU)
    n = 5
    while n > 0:
        print('Осталось покупок', n)
        user_choice = input('>>> ')
        if user_choice in ['1', '2', '3']:
            if user_choice == '1':
                hero['hp_max'] += 10
            if user_choice == '2':
                hero['dmg'] += 2
            if user_choice == '3':
                hero['crit_chance'] += 3
            n -= 1
        else:
            print('Ошибка, читать учись!')
        
    return hero

def game():
    '''
    Тут есть описание, просто его не видно)
    '''
    hero = gen_goblin()
    hero['name'] = 'Агроном, сын Арагорна'
    goblins = [
        gen_goblin(),
        gen_goblin(),
        gen_goblin(),
        gen_goblin(),
        gen_goblin()
    ]

    for goblin in goblins:
        for key, value in hero.items():
            print(key, value)
        hero = fight(hero, goblin)
        if hero['hp'] > 0:
            hero = shop(hero)
            hero['hp'] = hero['hp_max']
            # восстановить хп до максимального
            # вызвать магазин
        else:
            print('Game over')
            return
    print('Ты победил!')

game()