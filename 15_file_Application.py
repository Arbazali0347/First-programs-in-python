import os

def creat_file(filename):
    try:
        with open(filename,"x")as f:
            print(f"File Name {filename} Created Successfully ")
    except FileExistsError:
        print(f"Your File {filename} is Allready Existed!")
    except Exception as e:
        print("Not found File!")
def view_file():
    a = 1
    files = os.listdir()
    if not files:
        print("Files Not Found!")
    else:
        print("\nThis are all Files!")
        for i in files:
            print(f"{a} = {i}")
            a += 1
def delete_file(filename):
    try:
        os.remove(filename)
        print(f"File Name {filename} is Deleted Successfully")
    except FileNotFoundError:
        print(f'Your File {filename} is Not Found!')
    except Exception:
        print(f'File Error!')
def read_file(filename):
    try:
        with open(filename,"r")as f:
            content = f.read()
            print(f"\nThis Is Your content\n{content}")
    except FileNotFoundError:
        print(f'Your File {filename} is Not Found!')
    except Exception:
        print("file Error!")
def edit_file(filename,content):
    try:
        with open(filename,"a")as f:
            f.write(content)
            print("Your Content Edit successfully")
    except FileNotFoundError:
        print(f'Your File {filename} is Not Found!')
    except Exception:
        print("File ERROR")

def main():
    while True:
        print()
        print("1: Create File")
        print("2: View File")
        print("3: Delete File")
        print("4: Read File")
        print("5: Edit File")
        print("6: Exit Programe")

        choice = input("Enter Your Choice: ")
        if choice == "1":
            filename = input("Enter Your File Name: ")
            creat_file(filename)
        elif choice == "2":
            view_file()
        elif choice == "3":
            filename = input("Enter Your File Name: ")
            delete_file(filename)
        elif choice == "4":
            filename = input("Enter Your File Name: ")
            read_file(filename)
        elif choice == "5":
            filename = input("Enter Your File Name: ")
            content = input("Enter Edit Your Content: ")
            edit_file(filename,content)
        elif choice == "6":
            print("Ok Thanks Your Quiting System!")
            break
        else:
            print("Your Number is Valide!")
if __name__=="__main__":
    main()