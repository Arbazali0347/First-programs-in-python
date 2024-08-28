import random
import pyttsx3 
def gusse():
    computer = random.randint(1,100)
    a = -1
    b = 1
    engine = pyttsx3.init()
    while (a != computer):
        a = int(input("Enter your choice Number: "))
        if computer > a:
            print("higher Number please")
            b += 1
        elif computer < a:
            print("lower Number please")
            b += 1
    print(f"you are win and number this [{computer}] and your gusse attempts [{b}] ")
gusse()
