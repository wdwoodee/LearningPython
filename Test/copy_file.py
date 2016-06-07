def copyFile(oldFile,newFile):               
    f1 = open(oldFile,"r")
    f2 = open(newFile,"w")
    while 1:
        text = f1.read()
        if text == "": #如果f1没有字符时，则跳出循环
            break
        f2.write(text) #f1非空时，把text内容写到f2中
    f1.close()
    f2.close()
    return


if __name__ == "__main__":

    a = open("d:\\a.txt","w")
    a.write("what is your name?\n")
    a.write("My name is dwang!")
    a.close()
    b = open("d:\\b.txt","w")
    c = "d:\\a.txt"
    d = "d:\\b.txt"
    copyFile(c,d)
    f3 = open(c,"r")
    f4 = open(d,"r")
    print(f3.read())
    print()
    print(f4.read())
    f3.close()
    f4.close()
