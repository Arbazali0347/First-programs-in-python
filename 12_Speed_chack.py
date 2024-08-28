
from tkinter import *
from tkinter import filedialog
def chack():
    var = filedialog.askopenfile(title="MR BLACK",initialdir="/",
                                 filetypes=(("txt file","*.txt"),("all file","*.*")))
    print(var)
    



fram = Tk()
fram.title("Arbaz ** Speed Chack **")
fram.geometry("400x600")
fram.config(bg="grey")
fram.resizable(False,False)
text = Label(text="Internet Speed Chack",font=("Time New Roman",25,"bold"),bg="black",fg="white")
text.place(x=0,y=50,height=60,width=400)

text = Label(text="Download speed",font=("Time New Roman",20,"bold"),bg="black",fg="white")
text.place(x=35,y=140,height=60,width=330)

text_1 = Label(text="00",font=("Time New Roman",10,"bold"),bg="black",fg="white")
text_1.place(x=35,y=230,height=60,width=330)

text = Label(text="Uplaod Speed",font=("Time New Roman",20,"bold"),bg="black",fg="white")
text.place(x=35,y=320,height=60,width=330)

text_2 = Label(text="00",font=("Time New Roman",10,"bold"),bg="black",fg="white")
text_2.place(x=35,y=410,height=60,width=330)

button = Button(text="Click Chack",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus",bg="yellow",fg="black",command=chack)
button.place(x=35,y=500,height=60,width=330)
fram.mainloop()