# oops :-
# Class :- it is blueprint of objects or real world entity./collection of functions and objects 

class Mca:
    age = 20
    print("2024-26")

# # create object and class properties :-
x = Mca()
print(x.age)

# Q) create a class of name "age calculator", and take input of user dob and calculate the age in years.

class AgeCalculator:
    dob = int(input("Enter your year of birth : "))
    cd = int(input("Enter the current year : "))
    realage = cd - dob
n = AgeCalculator()
print("Your age is :", n.realage)


# POLYMORPHISM :- 
# Method overloading :- 

def age(dob1):
    print(dob1)

def age(dob,name):
    print(dob,name)

# x = age("19 oct 1991")
y = age("19 oct 1991", "Ekta")