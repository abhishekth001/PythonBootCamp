# Tuples can store the multiple data and data can't change 
myTuple = ("Amit", "Abhishek", "Arpit","Rishabh")
print(type(myTuple))
print(myTuple)


# To access a particular value 
print(myTuple[1])


# # can tupple change ?
myTuple[1] = "Harshit"
print(myTuple)

for x in myTuple:
    print(x)