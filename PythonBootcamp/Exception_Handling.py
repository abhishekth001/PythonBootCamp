# # Exception Handling


# print(x)

# try:
#     print(x)
# excep NameError:
#     print("something went wrong")



# x = 1/0
# print(x)



# try:
#    x = 1/0
#    print(x)
#    print(y)
# except ZeroDivisionError:
#     print("something went wrong")
# except NameError:
#     print("y is not defined")



# x = int(input("Enter the integer number"))
# y = str(x)

# z= ((y*7)/5)
# print(z)



# try:
#     x = int(input("Enter the integer number"))
#     y = str(x)
#     z= ((y*7)/5)
#     print(z)
#  except TypeError:
#     print("there is a type error")


# def inputAlphabetOnly(name):
#     while True:
#         user_input = input(name)
#         if user_input.isalpha():
#             return user_input
#         else:
#             print("Invalid input. Please enter alphabets only")
# name = inputAlphabetOnly("Enter your name: ")
# print(f"Hello, {name}!")


# # only numeric character allow

# def inputNumericOnly(number):
#     while True:
#         user_input = input(number)
#         if user_input.isnumeric():
#             return user_input
#         else:
#             print("Invalid input. Please enter numeric only")
# number = inputNumericOnly("Enter a number: ")
# print(f"Hello, {number}!")