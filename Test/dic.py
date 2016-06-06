__author__ = 'dwang'

# Python字典包含了以下内置函数：
# 1、cmp(dict1, dict2)：比较两个字典元素。
# 2、len(dict)：计算字典元素个数，即键的总数。
# 3、str(dict)：输出字典可打印的字符串表示。
# 4、type(variable)：返回输入的变量类型，如果变量是字典就返回字典类型。
# Python字典包含了以下内置方法：
# 1、radiansdict.clear()：删除字典内所有元素
# 2、radiansdict.copy()：返回一个字典的浅复制
# 3、radiansdict.fromkeys()：创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
# 4、radiansdict.get(key, default=None)：返回指定键的值，如果值不在字典中返回default值
# 5、radiansdict.has_key(key)：如果键在字典dict里返回true，否则返回false
# 6、radiansdict.items()：以列表返回可遍历的(键, 值) 元组数组
# 7、radiansdict.keys()：以列表返回一个字典所有的键
# 8、radiansdict.setdefault(key, default=None)：和get()类似, 但如果键不已经存在于字典中，将会添加键并将值设为default
# 9、radiansdict.update(dict2)：把字典dict2的键/值对更新到dict里
# 10、radiansdict.values()：以列表返回字典中的所有值

letterCounts = {}
for letter in "Mississippi":
    print(letter)
    letterCounts[letter] = letterCounts.get(letter, 0) + 1

print(letterCounts)

letterItem = letterCounts.items()
print("items list, letterItem: {0}".format(letterItem))
print(letterCounts.keys())
print(letterCounts.values())
print(letterCounts.get("p"))


#字典转化成tuple,list
dic = {'M': 1, 's': 4, 'p': 2, 'i': 4}
print(type(dic),str(dic))

print("tuple: {0}".format(tuple(dic.keys())))
print("tuple, values: {0}".format(tuple(dic.values())))

print("List: {0}".format(list(dic)))
print("List, values: {0}".format(list(dic.values())))

tup = (1,2,3,4,5)

print(tup.__str__())
print(str(tup))

print(list(tup))

ls = [1,2,3,4,5]
print("List to tuple: {0}".format(tuple(ls)))


#4、字符串

#字符串转为元组，返回：(1, 2, 3)
print(tuple(eval("(1,2,3)")))
#字符串转为列表，返回：[1, 2, 3]
print(list(eval("(1,2,3)")))
#字符串转为字典，返回：<type 'dict'>
print(type(eval("{'name':'ljq', 'age':24}")))