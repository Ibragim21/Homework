# Task1
# def divide_numbers(x, y):
#     try:
#         result = divmod(x,y)
#         print(f"Result: {result}")
#     except ZeroDivisionError:
#         print("The division by zero operation is not allowed.")

# x = int(input('enter numerator: '))
# y = int(input('enter denominator: '))
# divide_numbers(x,y)
# Task2
# def get_integer():
#     user_input = input("Please enter an integer: ")
#     user_integer = int(user_input)
#     print('Input is valid')
        
# try:
#     get_integer()
# except ValueError:
#     print("An error occurred: Invalid input.")
# Task3
# def find_file():
#     try:
#         file = open('testing.txt',mode='r')
#     except FileNotFoundError:
#         print('file does not exist')
# find_file()
# Task4
# def get_two_numbers():
#     try:
#         num1 = input("Please enter the first number: ")
#         num2 = input("Please enter the second number: ")
#         num1 = float(num1)
#         num2 = float(num2)
#         print(f"The first number is: {num1}")
#         print(f"The second number is: {num2}")
#     except ValueError:
#         raise TypeError("Both inputs must be numerical values.")

# try:
#     get_two_numbers()
# except TypeError as e:
#     print(f"An error occurred: {e}")
# Task5
# def reading_file():
#     with open("Homework5/test.txt", 'rt') as file:
#         text= file.read()
#         print(text) 
# try:
#     reading_file()
# except PermissionError:
#     print("You don't have permission to this file")
# Task6
# text= 'text for testing'
# index=int(input('enter an index for a word: '))
# def indexing():
#     print(text[index])
# try:
#     indexing()
# except IndexError:
#     print('Invalid index')
# Task7
# def get_number():
#     try:
#         user_input = input("Please enter a number: ")
#         number = float(user_input)
#         print(f"You entered the number: {number}")
#     except ValueError:
#         print("That is not a valid number! Please try again.")
#     except KeyboardInterrupt:
#         print("\nInput cancelled by user. Exiting the program.")

# try:
#     get_number()
# except KeyboardInterrupt:
#     print("\nProgram interrupted. Exiting...")
# Task8
def divide(a, b):
    try:
        result = a / b
        print(f"The result of {a} / {b} is {result}")
    except ArithmeticError as e:
        print(f"An error occurred: {e}")
numerator = float(input("Enter the numerator: "))
denominator = float(input("Enter the denominator: "))
divide(numerator, denominator)
# Task9
def reading_file():
    with open("Homework5/test.txt", 'rt') as file:
        text= file.read()
        print(text) 
try:
    reading_file()
except UnicodeDecodeError:
    print("UnicoDecodeError occured")
# Task10
def modify_list(my_list):
    try:
        my_list.append(10)
        print(my_list)
    except AttributeError as e:
        print(f"An error occurred: {e}")

my_list = [1, 2, 3, 4, 5]
modify_list(my_list)