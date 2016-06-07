def createFile():
    for i in range(1, 10):
        filename = "%d" % (i)
        f = open("d:\\1\\" + filename + ".txt", "w")
        f.close()
# can't be this
createFile()
