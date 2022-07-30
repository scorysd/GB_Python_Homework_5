# Создайте программу для игры в ""Крестики-нолики"".
import random
from time import sleep
def print_canv(mass):
    for i in mass:
        print(i, end='  ')
    print('  ')
def player_choice(players):
    player = random.choice(players)
    print(f'Первый ход достался: {player} \n{35 * "-"}\n') 
    move(player)
def move(player):
    print(f'{player}, твой ход. Куда пойдем?')
    step = None
    cell = None
    while step not in range(1, 10):
        step = int(input('Введите номер ячейки: '))
        if step not in range(1, 10):
            print(f"Такой ячейки нет. Соберись, {player}. Попробуй еще раз:")
    while step not in mass:
        print(f"Ячейка занята! Повнимательнее, {player}. Попробуй еще раз:")
        step = int(input('Введите номер ячейки: '))
    cell = mass.index(step) 
    if player == players[0]:
        mass[cell] = 'X'
    else:
        mass[cell] = 'O'
    print_canv(mass)
    
    check_result(player)
def check_result(player):
    if mass[1] == 'X' and mass[3] == 'X' and mass[5] == 'X' or mass[1] == 'O' and mass[3] == 'O' and mass[5] == 'O':
        print(f'Поздравляем, {player}!! Ты победил!! ')
    elif mass[9] == 'X' and mass[11] == 'X' and mass[13] == 'X' or mass[9] == 'O' and mass[11] == 'O' and mass[13] == 'O':
        print(f'Поздравляем, {player}!! Ты победил!! ')
    elif mass[17] == 'X' and mass[19] == 'X' and mass[21] == 'X' or mass[17] == 'O' and mass[19] == 'O' and mass[21] == 'O':
        print(f'Поздравляем, {player}!! Ты победил!! ')
    elif mass[1] == 'X' and mass[11] == 'X' and mass[21] == 'X' or mass[1] == 'O' and mass[11] == 'O' and mass[21] == 'O':
        print(f'Поздравляем, {player}!! Ты победил!! ')
    elif mass[5] == 'X' and mass[11] == 'X' and mass[17] == 'X' or mass[5] == 'O' and mass[11] == 'O' and mass[17] == 'O':
        print(f'Поздравляем, {player}!! Ты победил!! ')
    elif mass[1] == 'X' and mass[9] == 'X' and mass[17] == 'X' or mass[1] == 'O' and mass[9] == 'O' and mass[17] == 'O':
        print(f'Поздравляем, {player}!! Ты победил!! ')
    elif mass[3] == 'X' and mass[11] == 'X' and mass[19] == 'X' or mass[3] == 'O' and mass[11] == 'O' and mass[19] == 'O':
        print(f'Поздравляем, {player}!! Ты победил!! ')
    elif mass[5] == 'X' and mass[13] == 'X' and mass[21] == 'X' or mass[5] == 'O' and mass[13] == 'O' and mass[21] == 'O':
        print(f'Поздравляем, {player}!! Ты победил!! ')
    else:
        check_end_game(player)       
def player_change(player):
    if (players.index(player) + 2) > len(players):
        player = players[0]
        move (player)
    else:
        player = players[1]
        move (player)
def check_end_game (player):
    i = 0
    for i in range(len(mass)):
        if str(mass).isdigit():
            print('Ходов нет')
            break
        else:
            player_change(player)
global mass
mass = ['\n',1,'|',2,'|',3,'\n', '-------------', '\n', 4,'|', 5,'|', 6,'\n', '-------------', '\n', 7,'|', 8,'|', 9,'\n']
print(f'\n{70 * "-"}\n\n\n{30 * " "}PARTY TIME!!!\n\n\n{70 * "-"}')
sleep(5)
print(f'Пришло время поиграть!\nИграем в "крестики-нолики". \nНадеюсь, правила объяснять не нужно))')
pl_1 = input('Игрок №1, введите свое имя:\n').capitalize()
print(f'Приветствуем тебя, {pl_1}!')
pl_2 = input('Игрок №2, введите свое имя:\n').capitalize()
print(f'Приветствуем тебя, {pl_2}!')
players = [pl_1, pl_2]
print_canv(mass)
player_choice(players)