# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
import random
from time import sleep
def player_choice(players):
    player = random.choice(players)
    print(f'Первый ход достался: {player} \n{35 * "-"}\n') 
    move(player)
def check_result(player):
    if candys == 0:
        print(f'Поздравляем, {player}!! Ты победил!! ')
    else:
        player_change(player)
def move (player):
    print(f'{player}, твой ход. Сколько конфет возьмешь?')
    global candys 
    step = None
    print(f'На столе сейчас {candys} конфет(ы)')
    while step not in range(1, 29):
        step = int(input('Введите количество конфет: '))
        if step not in range(1, 29):
            print(f"Недопустимое значение. Соберись, {player}. Попробуй еще раз:")
    while step not in range(1, candys+1):
        print(f"{player}, ну ты чего?\nНа столе {candys} конфет(ы)\nКак ты можешь забрать {step}?\nПопробуй еще раз:")
        step = int(input('Введите количество конфет: '))
    candys = candys - step
    check_result(player)
def player_change(player):
    if (players.index(player) + 2) > len(players):
        player = players[0]
        move (player)
    else:
        player = players[1]
        move (player)
print(f'\n{70 * "-"}\n\n\n{30 * " "}PARTY TIME!!!\n\n\n{70 * "-"}')
sleep(5)
print(f'Пришло время поиграть!\nУсловие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.\nПервый ход определяется жеребьёвкой. \nЗа один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.')
pl_1 = input('Игрок №1, введите свое имя:\n').capitalize()
sleep(1)
print(f'Приветствуем тебя, {pl_1}!')
sleep(1)
pl_2 = input('Игрок №2, введите свое имя:\n').capitalize()
sleep(1)
print(f'Приветствуем тебя, {pl_2}!')
sleep(1)
players = [pl_1, pl_2]
candys = 2021
player_choice(players)