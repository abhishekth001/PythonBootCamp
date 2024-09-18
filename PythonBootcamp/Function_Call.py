# Functions in Python 

#create function to print statement
def myFunction():
    print("my function called")

#call the function by name
myFunction()


x = int(input("Enter Height "))
y= int(input("Enter Width "))
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