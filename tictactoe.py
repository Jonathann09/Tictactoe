print("=======================")
print("      Proggram by      ")
print("  Jonathan U. Urrete   ")
print("=======================")

from tkinter import *
from tkinter import messagebox
from random import randint

#GLOABAL VARIABLES
ActivePlayer=1
p1=[]# what player one selected
p2=[]# what player rwo selected
Count=0
ScoreX=0
ScoreO=0

root=Tk()
root.title("Tic Tac Toe :Player 1")
root.config(bg='light blue')
label1=Label(root,text='Tic Tac Toe',font="Times 15 bold",bg='cadet blue',fg='black',bd=4,height=2,width=10,relief=RAISED,)
label1.grid(row=0,column=1,padx=5,pady=5,sticky='nsnew')

label2=Label(root,text=f'SCORE-->PLAYER1: {ScoreX}\n-->PLAYER2: {ScoreO}',font="Times 15 bold",bg='cadet blue',fg='black',bd=4,height=1,width=10,relief=RAISED,)
label2.grid(row=4,column=0,padx=5,pady=5,sticky='nsnew')

label3=Label(root,text='PLAYER 1',font="Times 15 bold",bg='cadet blue',fg='black',bd=4,height=2,width=10,relief=RAISED,)
label3.grid(row=0,column=0,padx=5,pady=5,sticky='nsnew')

label4=Label(root,text='PLAYER 2',font="Times 15 bold",bg='white',fg='black',bd=4,height=2,width=10,relief=RAISED,)

#BUTTONS
b1=Button(root,text='',font="Times 35 bold",bg='white',fg='black',width=12)
b1.grid(row=1,column=0,padx=5,pady=5,sticky='snew')
b1.config(command=lambda:ButtonClick(1))