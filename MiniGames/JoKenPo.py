
from time import sleep
from random import randint

kws = ["\033[31mThe player loses!", "\033[32mThe player wins!", "\033[31minvalid choice!"]
items = ('Rock', 'Paper', 'Scissors') # Rock = 0, Paper = 1, Scissors = 2
bot = randint(0,2)
bar = "-" * 40 

print(f"JoKenPo!\n{bar}\n[ 0 ] Rock\n[ 1 ] Paper\n[ 2 ] Scissors")
move = int(input('Choice one: '))
print("Jo"), sleep(1), print("Ken"), sleep(1), print(f"Po!\n{bar}")
print(f'The bot chose: {items[bot]} \nThe player chose: {items[move]}')

if bot == 0: #bot chose rock
    if move == 0:
        print('\033[34mThe player and the bot chose: Rock! Tie.')
    elif move == 1:
        print(kws[1])
    elif move == 2:
       print(kws[0])
    else:
        print(kws[2])
        
if bot == 1: #Bot chose paper
    if move == 0:
        print(kws[0])
    elif move == 1:
        print('\033[34mThe player and the bot chose: Paper! Tie.')
    elif move == 2:
       print(kws[1])
    else:
        print(kws[2])

if bot == 2: #Bot chose scissors
    if move == 0:
        print(kws[1])
    elif move == 1:
        print(kws[0])
    elif move == 2:
        print('\033[34mThe player and the bot chose: Scissors! Tie.')
    else:
        print(kws[2])
