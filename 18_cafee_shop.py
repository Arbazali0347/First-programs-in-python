
from tkinter import messagebox as ms
def caffe():
    new = 0
    order = {
        "pizza": 500,
        "burger":400,
        "coffee":200,
        "figerchips":400,
        "chae":200,
        "biryani":500
        }
    print("00: Enter Quit!\n\n:Pizza = 500\n:Barger = 400\n:coffe = 400\n:Chae = 200\n:FingerChips = 400\n:Biryani = 500")
    while True:
        bye = input("Enter your order: ")
        if bye in order:
            new += order[bye]
            ms.showinfo("best message ","Thanks")
        elif bye == "00":
            print(f"You Tota Pay Rs:{new}")
            break
        else:
            print(f"Your Order is Not Avalibale!")
if __name__ == "__main__":
    caffe()