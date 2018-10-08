from Tkinter import *
#from ttk import *
import random
import sys
import tkMessageBox



def computerRandom():
    options = ["Rock","Paper","Scissors"]
    randomChoice = random.randint(0,2)
    computer_choice.set(options[randomChoice])
    return options[randomChoice]

def comparison(humanChoice, computerChoice):
    if humanChoice == computerChoice:
        return "Draw"
    if humanChoice == "Rock" and computerChoice == "Paper":
        return "Computer Wins"
    if humanChoice == "Paper" and computerChoice == "Scissors":
        return "Computer Wins"
    if humanChoice == "Scissors" and computerChoice == "Rock":
        return "Computer Wins"
    else: return "Human Wins"


    
def play() :
      humanChoice = player_choice.get()
      computerChoice =  computerRandom()
      
                     
      result = comparison (humanChoice, computerChoice)
            
      if result == "Draw":
            result_set.set("Its a Draw....Go Again!!")
      elif result == "Computer Wins":
            result_set.set("Unlucky you lost!")
      else:
            result_set.set("Well done you won!!!")

root=Tk()
root.title('Rock Paper Scissors')
root.config(bg='black')



player_choice = StringVar()
computer_choice = StringVar()
result_set=StringVar()
#player_choice.set("Rock")

photo1= PhotoImage(file="E:\python project\images\Rock.gif")
photo2= PhotoImage(file="E:\python project\images\Paper.gif")
photo3= PhotoImage(file="E:\python project\images\Scissors.gif")

Label(root, text='Player',font='Castellar 35 ',bg='black',fg='white').grid(column=1, row = 1, sticky = W,padx=20,pady=10)
Radiobutton(root, image=photo1,indicatoron=0, variable = player_choice, value = 'Rock',bg='black').grid(column=1, row=2, sticky=W,padx=20,pady=10)
Radiobutton(root, image=photo2,indicatoron=0, variable = player_choice, value = 'Paper',bg='black').grid(column=1, row=3, sticky=W,padx=20,pady=10)
Radiobutton(root, image=photo3,indicatoron=0, variable = player_choice, value = 'Scissors',bg='black').grid(column=1, row=4, sticky=W,padx=20,pady=10)

photo4= PhotoImage(file="E:\python project\images\Rock_computer.gif")
photo5=PhotoImage(file='E:\python project\images\Paper_computer.gif')
photo6=PhotoImage(file='E:\python project\images\Scissors_computer.gif')
Label(root, text='Computer',font='Castellar 35 ',bg='black',fg='white').grid(column=3, row = 1, sticky = W)
Radiobutton(root, image=photo4,indicatoron=0, variable = computer_choice, value = 'Rock',bg='black').grid(column=3, row=2, sticky=W,padx=20,pady=10)
Radiobutton(root,image=photo5,indicatoron=0, variable = computer_choice, value = 'Paper',bg='black').grid(column=3, row=3, sticky=W,padx=20,pady=10)
Radiobutton(root,image=photo6,indicatoron=0, variable = computer_choice, value = 'Scissors',bg='black').grid(column=3, row=4, sticky=W,padx=20,pady=10)

photo7=PhotoImage(file='play2.gif')
Button(root,image=photo7,command = play,bg='black',fg='black',bd=0).grid(column = 2, row = 2)

Label(root, textvariable = result_set,font=('Century725 Cn BT','20'),bg='black',fg='white').grid(column = 2, row = 6, columnspan = 2,sticky=W,padx=20)

Label(root,text='Choose Rock,Paper or Scissor...\n and Roll it',font=('Hobo Std','25',),bg='black',fg='white').grid(column=2,row=0)

root.mainloop()
