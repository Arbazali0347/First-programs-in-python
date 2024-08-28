

me = input("Enter your code: ")
me = me.split(" ")
code = input("Enter coding 1\nEnter dicoding 2\nEnter choice : ")
scrite = []
coding = True if (code == "1") else False
if (coding):
    sc_code = input("Enter your Scrite Key : ")
    new = []
    for word in me:
        if len(me)>=3:
            s1 ="gds"
            s2 = "fsd"
            words = s1 + word[2:] + word[0]+ word[1] +s2
            new.append(words)
        else:
            new.append(word[::-1])
    print(" ".join(new))
else:
    sc_code1 = input("Enter your Scrite key: ")
    if sc_code1.find(scrite):
        new = []
        for word in me:
            if len (me)>=3:
                words = word[3:-3]
                worder = words[-1] + words[:-1]
                worder1 = worder[-1] + worder[:-1]
                new.append(worder1)
            else:
                new.append(word[::-1])
        print(" ".join(new))
    else:
        print("your key is Not found")
#abazr ial ankh
