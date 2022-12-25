import customtkinter as ct
import random as rnd
import tkinter as tk
import time
from PIL import Image
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


# 50x50 Images
rock_img = tk.PhotoImage(file='Assets/Images/rock.png')
scissor_img = tk.PhotoImage(file='Assets/Images/scissor.png')
paper_img = tk.PhotoImage(file='Assets/Images/paper.png')
# 100x100 Images
rock_img_100 = tk.PhotoImage(file='Assets/Images/100/rock.png')
scissor_img_100 = tk.PhotoImage(file='Assets/Images/100/scissor.png')
paper_img_100 = tk.PhotoImage(file='Assets/Images/100/paper.png')

Choices_images = [rock_img,scissor_img,paper_img,rock_img_100,scissor_img_100,paper_img_100] # 0-2 50x50px - 3-5 100x100px

def play_screen():
    global AI_start
    global counter_lbl
    Buttons_frame.pack_forget()
    Welcome_lbl.pack_forget()
    counter_lbl = ct.CTkLabel(text=3,text_font=('Exlcluded',90))
    counter_lbl.after(1000,lambda: delay(2))
    counter_lbl.after(2000,lambda: delay(1))
    counter_lbl.after(3000, lambda: counter_lbl.pack_forget())
    counter_lbl.pack(anchor = tk.CENTER,pady=170)
    #===========================================================
    player_choices_frame = ct.CTkFrame(height=100,width=500,fg_color="#222325")
    player_choices_frame.pack(side = tk.BOTTOM,pady=30)
    Rock_btn = ct.CTkButton(player_choices_frame,image=rock_img,text="",width=50,height=50,fg_color="#222325",hover_color="#222325",command=lambda: Main_game('rock'))
    Rock_btn.grid(row = 0, column=0,padx=30)
    scissor_btn = ct.CTkButton(player_choices_frame,image=scissor_img,text="",width=50,height=50,fg_color="#222325",hover_color="#222325",command=lambda: Main_game('scissor'))
    scissor_btn.grid(row = 0, column=1,padx=30)
    paper_btn = ct.CTkButton(player_choices_frame,image=paper_img,text="",width=50,height=50,fg_color="#222325",hover_color="#222325",command=lambda: Main_game('paper'))
    paper_btn.grid(row = 0, column=2,padx=30)
    yourchoice_text = ct.CTkLabel(text='Choosse your choice',text_font=('Arial',18))
    yourchoice_text.pack(anchor=tk.CENTER,side = tk.BOTTOM)
    AI_choice_frame = ct.CTkFrame(fg_color="#222325")
    AI_choice_frame.pack(side=tk.TOP,pady=60)
    AI_choice_lbl = ct.CTkLabel(AI_choice_frame, text="",height=150,width=100)
    def AI_start():
        AI_choice_lbl.after(3500,lambda :AI_choice_lbl.configure(image = Choices_images[3]))
        AI_choice_lbl.after(3700,lambda:AI_choice_lbl.configure(image=Choices_images[4]))
        AI_choice_lbl.after(3900,lambda:AI_choice_lbl.configure(image=Choices_images[5]))
        AI_choice_lbl.after(4100,lambda :AI_choice_lbl.configure(image = Choices_images[3]))
        AI_choice_lbl.after(4300,lambda:AI_choice_lbl.configure(image=Choices_images[4]))
        AI_choice_lbl.after(4500,lambda:AI_choice_lbl.configure(image=Choices_images[5]))

    AI_choice_lbl.pack()
def after_choice():
    pass


def delay(sec):
    counter_lbl.configure(text=sec)
def exit():
    app.quit()

#=================== Labels ================#
Welcome_lbl = ct.CTkLabel(text= 'Welcome to Rock Paper Scissor Game',text_font=('Excluded',17,'bold'))
Welcome_lbl.pack(anchor = tk.CENTER,pady = 14)
Buttons_frame = ct.CTkFrame(fg_color="#222325")
Buttons_frame.pack(anchor=tk.CENTER,pady=120)
Play_btn = ct.CTkButton(Buttons_frame,text = "Play", text_font=('Excluded',17,'bold'), height=50,command=play_screen)
Play_btn.pack()
exit_btn = ct.CTkButton(Buttons_frame,text = "Exit", text_font=('Excluded',17,'bold'), height=50,command=exit)
exit_btn.pack(pady=15)




def Main_game(choice):
    AI_start()
    global Score
    global player_choice
    global AI_choice
    AI_choice = rnd.choice(Choices)
    player_choice = choice
    if player_choice=='rock' and AI_choice=='scissor': # p=rock, ai=scissor
        print(Think_msg)
        time.sleep(1)
        return player_choice
        print(f"A.I Choice: {AI_choice}\nYour Choice: {pla}")
        Score+=1 # should change the code for GUI
        print('BOOM! Rock Smashed the scissor')
    elif(player_choice=='rock' and AI_choice=='paper'):
        print(Think_msg)
        time.sleep(1)
        print(f"")


# while (not IsPlayerLost and Score<3):


app.mainloop( )