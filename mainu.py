print("....Welcome To Sups Health Managment....")
try:
    print("\tSelect to\n 1.view log 2.Add log")
    m1 = int(input())

    print("\tSelect client No =\n 1.Harry \n 2.Rohan \n 3.hamad")
    c1 = int(input())

    print("Select '1' for diet,\nSelect '2' for excersice =")
    c2 = int(input())


    def getdate():
        import datetime
        return datetime.datetime.now()

    if m1 == 1:
        if c1==3 and c2==1:
            f=open("hammD.txt","rt")
            j=f.read()
            print(j)
            f.close()
        else:
            f = open("hammE.txt", "rt")
            j = f.read()
            print(j)
            f.close()

        if c1 == 1 and c2 == 1:  # for harry diet
            f = open("HarryD.txt", "rt")
            h = f.read()
            print(h)
            f.close()
        if c1 == 1 and c2 == 2:  # for harry exe
            f = open("HarryE.txt", "r+")
            can = f.read()
            print(can)
            f.close()

        if c1 == 2 and c2 == 1:  # for rohan diet
            r = open("RohanD", "r+")
            can1 = r.read()
            print(can1)
            r.close()
        if c1 == 2 and c2 == 2:  # for rohan exe
            j = open("RohanE", "r+")
            can2 = j.read()
            print(can2)
            j.close()

    if m1 == 2:
        if c1 == 1 and c2 == 1:  # for harry diet
            f = open("HarryD.txt", "a")
            print("type your text")
            x = input()
            h = f.write(str(getdate()) + ": " + x + "\n")
            print("record save succefully")
            f.close()
        if c1 == 1 and c2 == 2:  # for harry diet
            f = open("HarryE.txt", "a")
            print("type your text")
            x = input()
            h = f.write(str(getdate())+":"+ x+"\n")
            print("record save succefully")
            f.close()
        if c1 == 2 and c2 == 1:  # for harry diet
            f = open("RohanD", "a")
            print("type your text")
            x = input()
            h = f.write(str(getdate())+":"+ x+"\n")
            print("record save succefully")
            f.close()
        if c1 == 2 and c2 == 2:
            f = open("RohanE", "a")
            print("type your text")
            x = input()
            h = f.write(str(getdate())+":"+ x+"\n")
            print("record save succefully")
            f.close()

        if c1 == 3 and c2 == 2:
            f = open("hammD.txt", "a")
            print("type here")
            x = input()
            h = f.write(str(getdate())+":"+ x+"\n")
            print("record save succefully")
            f.close()
        else:
            f = open("hammE.txt", "a")
            print("type here")
            x = input()
            h = f.write(str(getdate()) + ":" + x + "\n")
            print("record save succefully")
            f.close()
except Exception as e:
    print("Invalid input")

























