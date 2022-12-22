import customtkinter as ct
import random as rnd
import tkinter as tk
import time
app = ct.CTk()
app.title("Rock-Paper-Scissor Game")
app.resizable(False,False)
app.geometry('500x450')
IsPlayerLost = False
Score = 0
Think_msg='Computer is thinking...'
Counter_temp = 0
Choices = [
    'rock',
    'scissor',
    'paper'
]
def player_choice(choice):
    global Score
    global player_choice
    global AI_choice
    AI_choice = rnd.choice(Choices)
    player_choice = choice
    if player_choice=='rock' and AI_choice=='scissor': # p=rock, ai=scissor
        print(Think_msg)
        time.sleep(1)
        print(f"A.I Choice = {AI_choice}\nPlayer Choice={player_choice}")
        Score+=1 # should change the code for GUI
        print('BOOM! Rock Smashed the scissor')
    elif(player_choice=='rock' and AI_choice=='paper'):
player_choice('rock')