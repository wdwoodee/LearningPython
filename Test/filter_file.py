def filterFile(old,new):
    sfile = open(old,"r")
    dfile = open(new,"w")
    while 1:
        text = sfile.readline()
        if text == "":
            break
        elif text[0]  == "#":
            continue
        else:
            dfile.write(text)
    sfile.close()
    dfile.close()

if __name__== "__main__":
    c = "E:\\a.txt"
    d = "E:\\b.txt"
    wf1 = open(c,"w")
    wf1.write("12345\nwhat is your name\n#link you!\n\nsomething is wrong\n#ddddd!!!!")
    wf1.close()
    filterFile(c,d)
    rf1 = open(c,"r")
    rf2 = open(d,"r")
    print("This is a.txt")
    print(rf1.read())
    print("\n")
    print("This is b.txt, copy from a.txt")
    print(rf2.read())
    rf1.close()
    rf2.close()
    #print (f.read())
