print("Harsh")

#To print your name by using user input
name = input("Enter your name ")
print(name)


#WAP to find the current age
currentYear = int(input("Enter the current year"))
bornYear = int(input("Enter the born year"))
ageInYear = currentYear - bornYear
print(ageInYear)

# WAP for currency converter
# before starting
# input parameter required in programs
# e.g. in currency convertor u need currency amount
# in inr and converted currency index rate

print(" Convert ruppes into dollars")
ruppesAmount = int(input("Enter the amount in Rs. : "))
rsIntoDollar = (ruppesAmount / 84)
print(ruppesAmount, " convert into dollar ", rsIntoDollar)



print(" Convert dollar into ruppes")
dollarAmount = int(input("Enter the amount in Dollar. : "))
dollarIntoRs = (dollarAmount * 84)
print(dollarAmount, " convert into ruppes ", dollarIntoRs)


# WAP to check that you are eligible for voting or not
userAge = int(input("Enter your age"))
#for voting you must greater that 17
if(userAge > 17):
    print("Yor are eligible for voting")
else:
    print("Yor have to wait")



# WAP to check the user eligibile for job application
#if gender is female and age is greater then 17
#if gender is male then they can apply for private job


age = int(input("Enter your age "))
gender = input("Enter your Gender ")

# methor 1 :- 

if(age > 17):
    if(gender == 'female'):
        print("You are eligible for Government job")
    elif(gender == 'male'):
        print("You are eligible for private job")
    else:
        print("Your gender is incorrect")
else:
    print("You are not eligible for any job")
    
    
#method 2 :-
if(age > 17 and gender == "female"):
    print("You are eligible for Government job")
elif(age>17 and gender == "male"):
    print("Yor are eligible for private job")
else:
    print("You are not eligible for any job")



# WAP to Check the greatest number among 3 numbers

a = int(input(" Enter first value "))
b = int(input(" Enter second value "))
c = int(input(" Enter third value "))

if(a>b and a>c):
    print(a,"is greater then" , b ,"and" , c)
elif(b>c and b>a):
    print(b,"is greater then",a, "and", c)
else:
    print(c,"is greater then",a, "and",b)



#list, tupple, dictionary, are all similar in some conditions

#List:-
friendName = ["lokesh","Maninder","Ankit",1,2,3]
print(type(friendName))
print(friendName)


a=10
a+=10
a

a=10
b=20
a>b

a=10
b=20
a==b

a=10
b=20
a<b

a=10
b=20
a>=b

print(not(10))

print(not(0))

10 and 20

20 and 10

# Membership operator :-
# in and not in
a = 'This is my Python Class'
'P' in a

#### Day 3 ####

# LOOPS :-

friendName = ["lokesh","Maninder","Ankit",1,2,3]
#to add the new friend name in list
friendName.append("Dil bhardwaj")
#print after adding name
print("After", friendName)

# to add the name in specific position
friendName.insert(0,"Harsh")
#print after adding name at 0 index
print("After", friendName)

#to remove the name from list 
friendName.remove("Harsh")
print(friendName)

# remove last element from list
# Pop follow stack concept
friendName.pop()
print(friendName)

# we also pop any specific element from list
friendName.pop(2)
print(friendName)

# to sort the list
# it only sort only same type of data
friendName.sort()
print(friendName)

# #delete all names from list
# friendName.clear()
# print(friendName)

#for loop :-
# to print elements in the given list
for names in friendName:
    print(names)

# print the number 1 to 10
for i in range(1,11,1):
    print(i)

#print even number
# method 1 :-
for i in range(1,11,1):
    if(i%2==0):
        print(i)
        
#method 2 :-
for evenNo in range(2,11,2):
    print(evenNo)


# Tuples used to store the data and data is unchangeable and also non repeatable
sets = {"pawan","ivan","anshu","ivan"}
sets.add("harsh")
sets.remove("harsh")
sets[0] = "hgfd"
print(type(sets))
print(sets)


fname = ["Harsh","Lokesh","Maninder","Ankit","Ankur"]
fname.sort()
print(fname)

fname.reverse()
print(fname)


# print the current date and time 
import datetime
x= datetime.datetime.now()
print(x)


#present year
import datetime
x= datetime.datetime.now()
print(x.year)
# month/ day/ hour on the position 


#file
# to create new file and add my name also close the file
f = open("Abhishek.txt", "w")
f.write("My Name is Abhishek Thakur")
f.close()
f = open("Abhishek.txt","r")
print(f.read())

#enter your info in fime
#method 1 :-
f = open("myInfo.txt","w")
f.write(input("Enter your name: "))
f.write(input("Your cource: "))
f.write(input("Your college name: "))
f.close()


f=open("myInfo.txt","r")
print(f.read())


#method 2:-
f = open("h.txt","w")
name = input("Enter your name")
email = input("Enter your email")
collegeName = input("Enter your college name")
data = name + email + collegeName
f.write(data)
f.close
f = open("h.txt","r")
print(f.read())


# Use while loop to print 1 to 10
i=1
while i<5:
    print(i)
    i+=1

i=10
while i>0:
    print(i)
    i-=1

i=10
while i>0:
    print(i)
    break
    i-=1

#continue is use for escape
i=10
while i>0:
    print(i)
    i-=1
    continue


# Functions in Python ##

#create function to print statement
def myFunction():
    print("my function called")

#call the function by name
myFunction()


x = int(input("Enter Height "))
y= int(input("Enter Weidth "))
def findArea(x,y):
    area = x*y
    print("Area is : ",area)

#call
findArea(x,y)

    

x = int(input("Enter Height "))
y= int(input("Enter Weidth "))
def findArea(x,y):
    return x*y

#call
area = findArea(x,y)
print(area)




#  Write a Program to create 3 types of file:-
# 1. Jason File
# 2. Excel File
# 3. CSV File
# (read and write your data in all of them)

# taking input from user
name = input("Enter your name")
email = input("Enter your email")
collegeName = input("Enter your college name")
data = name + email + collegeName

# write data into json file :-
f = open("ht.json","w")
f.write(data)
f.close

# write data into Excel File :-
f = open("ht.xlsx","w")
f.write(data)
f.close

# wriet data into CSV file :-
f = open("ht.csv","w")
f.write(data)
f.close


f = open("ht.json","r")
print(f.read())

f = open("ht.xlsx","r")
print(f.read())

f = open("ht.csv","r")
print(f.read())




# Find the Factorial of a number by taking from user
num = int(input(" Enter a number to find its Factorial : "))

factorial = 1

# Calculate the factorial using a for loop
for i in range(1, num + 1):
    factorial *= i
    
print(f"The factorial of {num} is {factorial}")






# Tuples can store the multiple data and data can't change 
myTuple = ("Ekta", "Harsh", "Astha","Astha")
print(type(myTuple))
print(myTuple)

# # To access a particular value 
print(myTuple[1])

# # can tupple change ?
myTuple[1] = "Maninder"
print(myTuple)

for x in myTuple:
    print(x)


# Dictionary = It can store multiple data in key value pair
myDict = {
    "name" : "Abhishek",
    "age" : 20,
    "Mobile" : 8882600254
}

print(type(myDict))
print(myDict)

# # printing the values by for loop :-
for item in myDict:
    print(myDict[item])

# # To print the specific key :- 
print(myDict.get("name"))

# # To change the value of any key 
myDict["name"] = "Lokesh"
print(myDict)

# We use list for similar info. & use dictionary for different infos.

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