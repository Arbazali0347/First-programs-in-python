from tkinter import *
def main():
    print(frame2.tag_nextrange())
code = Tk()
code.geometry("500x600")
code.title("GAME")
code.config(bg="black")
frame = Label(bg="blue")
frame.place(x=25,y=30,height=100,width=450)
frame2 = Text(font=("Time New Roman",10,"bold"))
frame2.place(x=25,y=380,height=200,width=450)

frame1 = Text(font=("Time New Roman",10,"bold"))
frame1.place(x=25,y=150,height=200,width=450)

button = Button(code,text="Play Games",font=("Time New Roman",20,"bold"),relief=RAISED,command=main)
button.place(x=150,y=50,height=50,width=200)
code.mainloop()