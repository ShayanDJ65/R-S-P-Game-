import random as rnd
import time
import tkinter as tk

import customtkinter as ct

app = ct.CTk()
app.title("Rock-Paper-Scissor Game")
app.resizable(False, False)
app.geometry('500x450')
IsPlayerLost = False
Player_score = 0
AI_score = 0
Think_msg = 'Computer is thinking...'
Counter_temp = 0
Choices = [
    'rock',
    'scissor',
    'paper'
]

# 50x50 Images
rock_img = tk.PhotoImage(file='Assets/Images/rock.png')
scissor_img = tk.PhotoImage(file='Assets/Images/scissor.png')
paper_img = tk.PhotoImage(file='Assets/Images/paper.png')
# 100x100 Images
rock_img_100 = tk.PhotoImage(file='Assets/Images/100/rock.png')
scissor_img_100 = tk.PhotoImage(file='Assets/Images/100/scissor.png')
paper_img_100 = tk.PhotoImage(file='Assets/Images/100/paper.png')

Choices_images = [rock_img, scissor_img, paper_img, rock_img_100, scissor_img_100,
                  paper_img_100]  # 0-2 50x50px - 3-5 100x100px


def play_screen():
    global AI_start
    global counter_lbl
    global ai_msg
    global yourchoice_text
    global player_choices_frame
    global AI_choice_lbl
    Buttons_frame.pack_forget()
    Welcome_lbl.pack_forget()
    counter_lbl = ct.CTkLabel(text=3, text_font=('Exlcluded', 90))
    counter_lbl.after(1000, lambda: delay(2))
    counter_lbl.after(2000, lambda: delay(1))
    counter_lbl.after(3000, lambda: counter_lbl.pack_forget())
    counter_lbl.pack(anchor=tk.CENTER, pady=170)
    score_frame.pack(anchor=tk.N, padx=0, pady=10)
    Player_score_lbl.after(3050, lambda: Player_score_lbl.configure(text=f"Score: {Player_score}"))
    # AI_score_lbl.after(3050, lambda: AI_choice_lbl.configure(text=f" A.I Score: {AI_score}"))
    # ===========================================================
    player_choices_frame = ct.CTkFrame(height=100, width=500, fg_color="#222325")
    player_choices_frame.pack(side=tk.BOTTOM, pady=30)
    rock_btn = ct.CTkButton(player_choices_frame, image=rock_img, text="", width=50, height=50, fg_color="#222325",
                            hover_color="#222325", command=lambda: Main_game('rock'))
    rock_btn.grid(row=0, column=0, padx=30)
    scissor_btn = ct.CTkButton(player_choices_frame, image=scissor_img, text="", width=50, height=50,
                               fg_color="#222325", hover_color="#222325", command=lambda: Main_game('scissor'))
    scissor_btn.grid(row=0, column=1, padx=30)
    paper_btn = ct.CTkButton(player_choices_frame, image=paper_img, text="", width=50, height=50, fg_color="#222325",
                             hover_color="#222325", command=lambda: Main_game('paper'))
    paper_btn.grid(row=0, column=2, padx=30)
    yourchoice_text = ct.CTkLabel(text='Choosse your choice', text_font=('Arial', 18))
    yourchoice_text.pack(anchor=tk.CENTER, side=tk.BOTTOM)
    AI_choice_frame = ct.CTkFrame(fg_color="#222325")
    AI_choice_frame.pack(side=tk.TOP, pady=66)
    AI_choice_lbl = ct.CTkLabel(AI_choice_frame, text="", height=100, width=100)
    ai_msg = ct.CTkLabel(text='', text_font=('Excluded', 19))

    def AI_start():
        AI_choice_lbl.after(300, lambda: AI_choice_lbl.configure(image=Choices_images[3]))  # 3500
        AI_choice_lbl.after(450, lambda: AI_choice_lbl.configure(image=Choices_images[4]))  # +200
        AI_choice_lbl.after(600, lambda: AI_choice_lbl.configure(image=Choices_images[5]))
        AI_choice_lbl.after(750, lambda: AI_choice_lbl.configure(image=Choices_images[3]))
        AI_choice_lbl.after(900, lambda: AI_choice_lbl.configure(image=Choices_images[4]))
        AI_choice_lbl.after(1050, lambda: AI_choice_lbl.configure(image=Choices_images[5]))
        # --
        AI_choice_lbl.after(1200, lambda: AI_choice_lbl.configure(image=Choices_images[3]))  # 4600
        AI_choice_lbl.after(1350, lambda: AI_choice_lbl.configure(image=Choices_images[4]))  # +300
        AI_choice_lbl.after(1500, lambda: AI_choice_lbl.configure(image=Choices_images[5]))
        AI_choice_lbl.after(1650, lambda: AI_choice_lbl.configure(image=Choices_images[3]))

    AI_choice_lbl.pack()


def after_choice():
    pass


def ai_msg(text):
    ai_msg.configure(text=text)


def delay(sec):
    counter_lbl.configure(text=sec)


def exit():
    app.quit()


# =================== Labels ================#
Welcome_lbl = ct.CTkLabel(text='Welcome to Rock Paper Scissor Game', text_font=('Excluded', 17, 'bold'))
Welcome_lbl.pack(anchor=tk.CENTER, pady=14)
Buttons_frame = ct.CTkFrame(fg_color="#222325")
Buttons_frame.pack(anchor=tk.CENTER, pady=120)
Play_btn = ct.CTkButton(Buttons_frame, text="Play", text_font=('Excluded', 17, 'bold'), height=50, command=play_screen)
Play_btn.pack()
exit_btn = ct.CTkButton(Buttons_frame, text="Exit", text_font=('Excluded', 17, 'bold'), height=50, command=exit)
exit_btn.pack(pady=15)
score_frame = ct.CTkFrame(height=500, width=5000, fg_color="#222325")
Player_score_lbl = ct.CTkLabel(score_frame, text="", text_font=('Excluded', 27))
Player_score_lbl.pack(anchor=tk.NW)


# AI_score_lbl = ct.CTkLabel(score_frame,text="",text_font = ('Excluded', 22))
# AI_score_lbl.pack(anchor=tk.N)

def Main_game(choice):
    AI_start()
    global Player_score
    global player_choice
    global AI_choice
    AI_choice = 'paper'
    # AI_choice = rnd.choice(Choices)
    player_choice = 'rock'  # should change to choice after test
    if player_choice == 'rock' and AI_choice == 'scissor':  # p=rock, ai=scissor player scores
        yourchoice_text.pack_forget()
        player_choices_frame.pack_forget()
        print(Think_msg)
        print(f"A.I Choice: {AI_choice}\nYour Choice: {player_choice}")
        score_cal(1)
        # Player_score += 1  # should change the code for GUI
        AI_choice_lbl.after(1800, lambda: AI_choice_lbl.configure(image=rock_img_100))
        Player_score_lbl.configure(text=f"Score: {Player_score}")
        ai_msg.configure(text='BOOM! Rock Smashed the scissor. Rock wins!')
        ai_msg.after(1810, lambda: ai_msg.pack(side=tk.BOTTOM, pady=50))
        ai_msg.after(3000, lambda: ai_msg.pack_forget())
        # print('BOOM! Rock Smashed he scissor')
        player_choices_frame.after(2000, lambda: player_choices_frame.pack(side=tk.BOTTOM, pady=30))
        yourchoice_text.after(2000, lambda: yourchoice_text.pack(anchor=tk.CENTER, side=tk.BOTTOM))
    elif player_choice == 'rock' and AI_choice == 'paper':  # ai scores
        yourchoice_text.pack_forget()
        player_choices_frame.pack_forget()
        print(Think_msg)
        print(f"A.I Choice: {AI_choice}\nYour Choice: {player_choice}")
        score_cal(1)
        # Player_score -= 1  # should change the code for GUI
        AI_choice_lbl.after(1800, lambda: AI_choice_lbl.configure(image=paper_img_100))
        Player_score_lbl.configure(text=f"Score: {Player_score}")
        ai_msg.configure(text='Oops! Paper covers rock; paper wins')
        ai_msg.after(1810, lambda: ai_msg.pack(side=tk.BOTTOM, pady=50))
        ai_msg.after(3000, lambda: ai_msg.pack_forget())
        player_choices_frame.after(2000, lambda: player_choices_frame.pack(side=tk.BOTTOM, pady=30))
        yourchoice_text.after(2000, lambda: yourchoice_text.pack(anchor=tk.CENTER, side=tk.BOTTOM))
    elif player_choice == 'paper' and AI_choice == 'rock': # player scores
        yourchoice_text.pack_forget()
        player_choices_frame.pack_forget()
        print(Think_msg)
        print(f"A.I Choice: {AI_choice}\nYour Choice: {player_choice}")
        Player_score += 1  # should change the code for GUI
        AI_choice_lbl.after(1800, lambda: AI_choice_lbl.configure(image=paper_img_100))
        Player_score_lbl.configure(text=f"Score: {Player_score}")
        ai_msg.configure(text='Well Done! Paper covers rock; paper wins')
        ai_msg.after(1810, lambda: ai_msg.pack(side=tk.BOTTOM, pady=50))
        ai_msg.after(3000, lambda: ai_msg.pack_forget())
        player_choices_frame.after(2000, lambda: player_choices_frame.pack(side=tk.BOTTOM, pady=30))
        yourchoice_text.after(2000, lambda: yourchoice_text.pack(anchor=tk.CENTER, side=tk.BOTTOM))

def score_cal(num):
    global Player_score
    if Player_score>0:
        Player_score=Player_score+num
# while (not IsPlayerLost and Player_score<3):


app.mainloop()
