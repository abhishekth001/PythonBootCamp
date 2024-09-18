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

