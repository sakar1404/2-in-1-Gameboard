import sys
import os
from Tkinter import *
import tkMessageBox
root=Tk()
root.geometry('650x550')
root.config(bg='black')

tkMessageBox.showinfo(title='Credits',message='Name:- Sakar Kardekar \n Enroll No. :- 151375 \n Batch:- B5 \n Mob. No. :-8982087189 \n Email id :- sakar.kardekar@gmail.com')

Label(root,text='2 in 1 Game Board',font=('Castellar 30 bold'),bg='black',fg='white').grid(columnspan=2,column=0,row=0,sticky=W+E+S+N)


Label(root,text='Which game you want to play?',font=('Hobo Std','25',),bg='black',fg='white').grid(columnspan=3,column=0,row=1,pady=50)



Label(root,text='Rock Paper Scissor',font=('ALGERIAN','20'),bg='black',fg='white').grid(column=0,row=2)




Label(root,text='Guess the Colour',font=('ALGERIAN','20'),bg='black',fg='white').grid(column=1,row=2)

Label(root,text='  ',bg='black',fg='white').grid(column=0,row=4,pady=30)

Label(root,text='Not interested now?Press Exit',font=('Century725 Cn BT','12'),bg='black',fg='white').grid(column=0,row=5,sticky=SW)

def exitgame():
    if  tkMessageBox.askokcancel('EXIT','are you sure?'):
        root.destroy()
photo5=PhotoImage(file='E:\python project\images\exit.gif')
Button(root,image=photo5,command=exitgame).grid(column=1,row=5,sticky=SE)

def game1():
    os.system('python rps.py')

photo1=PhotoImage(file='E:\python project\images\logo2.gif')
b1=Button(root,image=photo1,command= game1)
b1.grid(pady=8,column=0,row=3,padx=20)

def game2():
      os.system('python colour.py')

photo2=PhotoImage(file='E:\python project\images\color.gif')
b2=Button(root,image=photo2,command=game2)
b2.grid(pady=8,column=1,row=3,padx=20)



root.mainloop()
