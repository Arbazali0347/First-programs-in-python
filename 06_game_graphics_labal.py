from tkinter import *
frame = Tk()
frame.geometry("500x500")
frame.title("Mr Aro Gmaing")
frame.config(bg="grey")
text = Label(frame,text="MR ARO GAMING",font=("Time New Roman",30),bg="grey")
text.place(x=85,y=50,width=330,height=60)
type1 = Text(font=("Time New Roman",10),wrap=WORD,)
type1.place(x=30,y=100,height=190,width=440)
bt = Button(frame,bg="red",text="click",font=("Time New Roman",20,"bold"),relief=RAISED)
bt.place(x=180,y=300,widt=150,height=40)

frame.mainloop()