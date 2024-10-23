import pygame
import random
import time
players_2 = False
print('Welcome to the NIM game')
how_many = input('Will there be "1" or "2" Players?')

def lose(name, name1, name2):
    if players_2 == True:
        print("Player 2 wins")     
    else:
        print(name, 'loses')
        print('THE CPU HAS WON')

def win(name, name1, name2):
    if players_2 == True:
        print(name1, 'wins!')
    else:
        print(name, 'wins!')

def nameVScpu():
    name = (input('What is your name? ')) 
    print('You will now be matched against a bot')
    
def nameFOR2():
    name1 = (input('What is the name of player 1? '))
    time.sleep(0.3)
    name2 = (input('What is the name of player 2? '))
    time.sleep(0.5)
    print('game will begin soon')

if how_many == '1':
    players_2 = False
    nameVScpu()
elif how_many == '2':
    players_2 = True
    nameFOR2()
else:
    print('Invalid Input')