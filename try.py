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
try:
    list1 = [1, 2]
    guess = int(input("Guess how many items are in the list: "))
    
    if guess == len(list1):
        for i in list1:
            print(i)
except IndexError: 
    print(f"The list is: {list1}")
    print("There is no more.")