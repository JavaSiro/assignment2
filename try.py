#b
# try:
#     firstnumber = int(input("Enter the first number: "))
#     secondnumber = int(input("Enter the the second number: "))
#     result = firstnumber/secondnumber
#     print(f"Result is: {result}")
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")
# except ValueError:
#     print("Error: Please enter valid numbers.")

#c
# try:
#     list=[1,2,3]
#     for i in range(0,5):
#         print(list[i])
# except:
#     print('not more than this')

#d
# list=[1,'1',1.1,True]
# n=-5
# for i in list:
#     try:
#         print(i+n)
#     except:
#         print("nahh u can't do that with this tyoe of data")

#e
# try:
#     number=float(input('type number: '))
#     print(number)
# except:
#     print('u gotta type in only numbers')

#f
# textnamesearch = input('Search a .txt file by typing the name of it: ')
# try:
#     with open(textnamesearch, 'r') as file:
#         content = file.read()
#         print(f"Content of '{textnamesearch}':   ")
#         print(content)
# except:
#     print('No such file.')

#g
# key = input("search a car: ")
# di = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
# try:
#     print(di[key])
# except:
#     print("no such car!")