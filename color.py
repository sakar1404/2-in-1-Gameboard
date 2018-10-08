from Tkinter import *
import random
from tkMessageBox import *

colours = ['Red','Blue','Green','Pink','Black','Yellow','Orange','White','Purple','Brown']

score=0
timeleft=30
def startGame(event):
    if timeleft == 30:       
        countdown()   
    nextColour()


def nextColour():
    global score
    global timeleft
    if timeleft > 0:       
        e.focus_set()        
        if e.get().lower() == colours[1].lower():     
            score += 1
        e.delete(0,END)   
        random.shuffle(colours)   
        label.config(fg=str(colours[1]), text=str(colours[0]))       
        scoreLabel.config(text="Score: " + str(score))
    
        

def countdown():    
    global timeleft
    if timeleft > 0:
        timeleft -= 1
        timeLabel.config(text="Time left: " + str(timeleft)) 
        timeLabel.after(1000, countdown)
    else:
        showerror(title='Times up!!',message='Your times up!!')
root =Tk()
root.config(bg='grey')
root.title("The Colour Game..")

root.geometry("650x400")

instructions =Label(root, text="Type in the colour of the words, and not the word text!",font=('Harrington','19','bold'),bg='grey')
instructions.grid(row=0,column=0,pady=10,sticky=W+E+N+S)
scoreLabel =Label(root, text="Press Enter to start",font=('Hobo Std','14','bold'),bg='grey')
scoreLabel.grid(row=1,column=0,pady=10,sticky=W+E+N+S)

timeLabel =Label(root, text="Time left: " + str(timeleft), font=('Century725 Cn BT','14'),fg='Red',bg='grey')
timeLabel.grid(row=2,column=0,pady=10,sticky=W+E+N+S)

label =Label(root, font=('Algerian', 60),bg='grey')
label.grid(row=3,column=0,pady=10,sticky=W+E+N+S)

e =Entry(root)

root.bind('<Return>', startGame)
e.grid(row=4,column=0,pady=10)

e.focus_set()

def finalscore():
    showinfo(title='Final Score',message='Your score is: '+str(score))

button1=Button(root,text='Score',padx=20,command=finalscore,bg='black',fg='white')
button1.grid(row=5,column=0,pady=10)


root.mainloop()
