def find(find_string, ch):
    index = 0
    while index < len(find_string):
        if find_string[index] == ch:
            return index+1   #找到后返回index值，并退出循环
        index += 1
    return -1 #找不到程序正常结束

def find2(find_string, ch):
    index = 0
    j = []  #记录出现的位置
    while index < len(find_string):
        if find_string[index] == ch:
            j.append(index+1)   #找到后返回index值，并退出循环
        index += 1
    return j #返回出现

def find3(find_string, ch):
    index = 0
    count = 0
    while index < len(find_string):
        if find_string[index] == ch:
            count += 1
        index += 1
    return count #返回出现的次数

strin = "abcdefghijkldimn"
c = "d"
print(find(strin,c))
print(find2(strin,"d"))
print(find3(strin,"d"))

