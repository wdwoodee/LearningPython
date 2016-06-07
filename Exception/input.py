# while True:
# 	try:
# 		s = int(input("Please enter a number:"))
# 		break
# 	except ValueError:
# 		print("Oops! That was no valid numbser. Try again.....")
# # s = int(input("enter a ndumber:"))


# while True:
# lst = ["dwang","wangdong","netgbrain"]
lst = [2,4,0,4,0,8]
for i in lst:
    try:
        print(i)
        t = 16/i
        print(t)
    except ZeroDivisionError:
        print('excetion')


# print(3/0)
